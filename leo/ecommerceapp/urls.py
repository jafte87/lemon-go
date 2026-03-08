from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store', views.store, name='store'),
    path('aboutus', views.about_us, name='aboutus'),
    path('players', views.players, name='players'),
]