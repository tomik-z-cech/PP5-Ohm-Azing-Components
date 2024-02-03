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
    
    # Set variable for sizes and values
    HAS_SIZES = ((0, "No - Item has no sizes"), (1, "Yes - Item has different sizes"))
    HAS_VALUES = ((0, "No - Item has no values"), (1, "Yes - Item has different values"))
    
    item_category = models.ManyToManyField(Category, blank=False, help_text='Select more categories by CTRL + click')
    item_name = models.CharField(max_length=254)
    item_sku = models.CharField(max_length=254, null=True, blank=False)
    item_description = models.TextField(blank=False)
    different_sizes = models.IntegerField(choices=HAS_SIZES, default=0, help_text='Select yes if item comes in different package sizes')
    sizes = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text='Separate sizes by comma ","')
    different_values = models.IntegerField(choices=HAS_VALUES, default=0, help_text='Select yes if item comes in different values')
    values = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text='Separate values by comma ","')
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    image_1 = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="category_images/", force_format='WEBP', blank=True)
    image_2 = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="category_images/", force_format='WEBP', blank=True)
    image_3 = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="category_images/", force_format='WEBP', blank=True)

    def __str__(self):
        return self.item_name