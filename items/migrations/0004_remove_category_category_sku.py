# Generated by Django 4.2.7 on 2024-01-30 14:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0003_category_category_sku"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="category_sku",
        ),
    ]
