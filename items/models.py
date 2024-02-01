from django_resized import ResizedImageField
from django.db import models

# Create your models here.
class Category(models.Model):

    category_name = models.CharField(max_length=254)
    category_image = ResizedImageField(size=[400, 400], crop=['middle', 'center'], quality=75, upload_to="media/category_images/", force_format='WEBP', blank=True)

    def __str__(self):
        return self.category_name
