from django.contrib import admin
from .models import Produit, ImageProduit
from .models import Media


class ImageInline(admin.TabularInline):
    model = ImageProduit
    extra = 1
    fields = ('image',)

@admin.register(Produit)

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    search_fields = ('nom',)

    inlines = [ImageInline]

@admin.register(ImageProduit)

class ImageProduitAdmin(admin.ModelAdmin):
    list_display = ('produit', 'image')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fichier')

    
            


