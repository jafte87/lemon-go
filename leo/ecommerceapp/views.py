from django.shortcuts import render


def store(request):
    return render(request, 'store.html')
def index(request):
    return render(request, 'index.html')
def about_us(request):
    return render(request, 'aboutus.html')
def players(request):
    return render(request, 'players.html')
# Create your views here.
