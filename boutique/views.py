from django.shortcuts import render
from .models import Produit, Media

def home(request):
    return render(request, 'index.html')

def produits(request):
    produits = Produit.objects.all()
    medias = Media.objects.all()
    return render(request, 'produits.html', {
        'produits': produits,
        'medias': medias
        })



