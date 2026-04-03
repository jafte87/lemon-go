from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Product, Cart, CartItem

def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart',{})

    product_id_str = str(product_id)

    if product_id_str in cart :
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    
    request.session['cart'] = cart
    return redirect('store')

def store(request):
    products = Product.objects.all()
    return render(request, 'store.html', {'products': products})

def view_cart(request):

    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id))
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })
    
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })
def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        messages.success(request, 'Item has been removed')
    
    return redirect('view_cart')

def signup(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created')
            return redirect('store')
        else:
            messages.error(request, 'Invalid informations')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f' Welcome!{username} ')
            
            next_url = request.GET.get('next', 'store')
            return redirect(next_url)
        else:
            messages.error(request, 'Wrong username or Password')
    
    return render(request, 'signin.html')

def signout(request):

    logout(request)
    messages.success(request, 'loged out')
    return redirect('store')

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'aboutus.html')

def players(request):
    return render(request, 'players.html')
