# Generated by Django 4.2.7 on 2024-02-12 15:55

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("profilemanager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=["middle", "center"],
                force_format="WEBP",
                keep_meta=True,
                quality=75,
                scale=None,
                size=[300, 300],
                upload_to="profile_pictures/",
            ),
        ),
    ]
