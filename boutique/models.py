from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    DEVISE_CHOICES = (
        ('USD', '$'),
        ('CDF', 'FC'),
    )

    devise = models.CharField(max_length=3, choices=DEVISE_CHOICES, default='USD')

    def __str__(self):
        return self.nom


class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='galerie/')
    
    def __str__(self):
        return f"Image de {self.produit.nom}"

class Media(models.Model):
    TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to='galerie/')

    def __str__(self):
        return self.type
