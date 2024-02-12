# Generated by Django 4.2.7 on 2024-02-12 09:33

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_resized.forms


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50, null=True)),
                ("last_name", models.CharField(max_length=50, null=True)),
                ("phone_number", models.CharField(max_length=20, null=True)),
                ("marketing", models.BooleanField()),
                (
                    "profile_picture",
                    django_resized.forms.ResizedImageField(
                        blank=True,
                        crop=["middle", "center"],
                        force_format="WEBP",
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[300, 300],
                        upload_to="item_images/",
                    ),
                ),
                ("address_1", models.CharField(max_length=100, null=True)),
                ("address_2", models.CharField(max_length=100, null=True)),
                ("city", models.CharField(max_length=50, null=True)),
                ("county", models.CharField(max_length=50, null=True)),
                ("post_code", models.CharField(max_length=15, null=True)),
                (
                    "country",
                    django_countries.fields.CountryField(max_length=2, null=True),
                ),
                (
                    "user_wishlist",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=254),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "username",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
            },
        ),
    ]
