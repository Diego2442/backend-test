from django.db import models
from django.utils.text import slugify


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.nombre}'

    def save(self, *args, **kwargs):
        # Siempre genera un nuevo slug cuando se guarda
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)