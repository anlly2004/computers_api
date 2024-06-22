from django.db import models

# Create your models here.
class Marca(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255, blank=True, null=True)

class Monitor(models.Model):
    color = models.CharField(max_length=255)
    contrast= models.DateField(null=True, blank=True)
    shine = models.DateField(null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

class Procesador(models.Model):
    name = models.CharField(max_length=255)
    generations = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

class DiscoDuro(models.Model):
    guys = models.CharField(max_length=255)
    ability = models.DateField(null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    

