from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Product name')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name= 'Price')
    image = models.CharField(
    max_length=100,
    verbose_name='product image',
    null=True,
    blank=True
    )
    description = models.TextField(verbose_name='Product description', blank=True)
    stock = models.IntegerField(default=0, verbose_name='Available amount')
    created_at = models.DateField(auto_now_add=True, verbose_name='Adding history')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
        null=True,
        blank=True
    )
    session_key =models.CharField(max_length=255, null=True, blank=True, verbose_name='session key')
    created_at = models.DateField(auto_now_add=True, verbose_name='Creation date')
    updated_at = models.DateField(auto_now=True, verbose_name='Update time')

    def get_total_price(self):
        total = sum(item.get_total_price() for item in self.items.all())
        return total
    
    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())
    
    def __str__(self):
        if self.user:
            return f'Cart {self.user.username}'
        return f'Cart {self.session_key}'
    class Meta:
        verbose_name= 'Cart'
        verbose_name_plural= 'Carts'
    
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Cart'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Product'
    )

    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Quantity'
    )

    def get_total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
    class Meta:
        verbose_name='Cart item'
        verbose_name_plural='Cart items'
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'product'], 
                name='unique_cart_product'
            )
        ]


class Order(models.Model):
    STATUS_CHOICES = [
    ('pending', 'قيد الانتظار'),
    ('paid', 'مدفوع'),
    ('shipped', 'تم الشحن'),
    ('delivered', 'تم التسليم'),
    ('cancelled', 'ملغي'),
    ]
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="User"
    )
    first_name = models.CharField(max_length=100, verbose_name="First name")
    last_name = models.CharField(max_length=100, verbose_name="Last name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Phone number")
    address = models.TextField(verbose_name="Adress")
    city = models.CharField(max_length=100, verbose_name="City")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=" Total price")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Order history")
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

