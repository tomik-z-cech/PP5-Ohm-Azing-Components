from django_resized import ResizedImageField
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Category(models.Model):

    category_name = models.CharField(max_length=254)
    category_image = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="category_images/", force_format='WEBP', blank=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Item(models.Model):
    item_category = models.ManyToManyField(Category, blank=False)
    item_name = models.CharField(max_length=254)
    item_sku = models.CharField(max_length=254, null=True, blank=False)
    item_description = models.TextField(blank=False)
    different_sizes = models.BooleanField(default=False, null=True, blank=True)
    sizes = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    different_values = models.BooleanField(default=False, null=True, blank=True)
    values = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    image_1 = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="category_images/", force_format='WEBP', blank=True)
    image_2 = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="category_images/", force_format='WEBP', blank=True)
    image_3 = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="category_images/", force_format='WEBP', blank=True)

    def __str__(self):
        return self.item_name