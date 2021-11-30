from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Link(models.Model):
    key =  models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = URLField(verbose_name="Enlace", max_length=200,null=True, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ["-name"]
    
    def __str__(self):
        return self.name