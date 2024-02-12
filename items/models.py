from django_resized import ResizedImageField
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

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
    VAT_RATES = ((0, "23 % VAT"), (1, "13.5 % VAT"), (2, "9 % VAT"), (3, "0 % VAT"))
    
    item_sku = models.CharField(max_length=254, null=True, blank=False)
    item_name = models.CharField(max_length=254, unique=True)
    item_description = models.TextField(blank=False)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    item_vat_rate = models.IntegerField(choices=VAT_RATES, default=0)
    item_category = models.ManyToManyField(Category, blank=False, help_text='Select more categories by CTRL + click')
    different_sizes = models.IntegerField(choices=HAS_SIZES, default=0, help_text='Select yes if item comes in different package sizes')
    sizes = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text='Separate sizes by comma ","')
    different_values = models.IntegerField(choices=HAS_VALUES, default=0, help_text='Select yes if item comes in different values')
    values = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text='Separate values by comma ","')
    image_1 = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="item_images/", force_format='WEBP', blank=True)
    image_2 = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="item_images/", force_format='WEBP', blank=True)
    image_3 = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="item_images/", force_format='WEBP', blank=True)
    item_stock = models.IntegerField(default=0)
    item_likes = models.ManyToManyField(User, related_name="item_likes", blank=True)
    item_dislikes = models.ManyToManyField(User, related_name="item_dislikes", blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

