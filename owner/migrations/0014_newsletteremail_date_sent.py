# Generated by Django 4.2.7 on 2024-02-24 20:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("owner", "0013_newsletteremail_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsletteremail",
            name="date_sent",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
