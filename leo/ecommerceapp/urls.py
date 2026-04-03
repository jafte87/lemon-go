from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store', views.store, name='store'),
    path('aboutus', views.about_us, name='aboutus'),
    path('players', views.players, name='players'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),

]