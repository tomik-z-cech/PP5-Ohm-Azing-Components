from django.db import models

# Create your models here.
class Category(models.Model):

    category_name = models.CharField(max_length=254)
    category_image = models.ImageField(null=True, blank=True)
    category_code = models.CharField(max_length=3)

    def __str__(self):
        return self.category_name
   