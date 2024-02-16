# Generated by Django 4.2.7 on 2024-02-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("owner", "0004_invoice_date_added"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostageSettings",
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
                ("free_postage", models.IntegerField()),
                ("standard_cost", models.IntegerField()),
            ],
        ),
    ]
