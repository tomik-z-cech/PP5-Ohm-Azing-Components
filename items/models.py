from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=254)
    slug_name = models.SlugField(max_length=255, unique=True, blank=True)
    category_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    