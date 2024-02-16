# Generated by Django 4.2.7 on 2024-02-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("owner", "0007_postagesettings_express_cost"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="postagesettings",
            name="express_cost",
        ),
        migrations.RemoveField(
            model_name="postagesettings",
            name="standard_cost",
        ),
        migrations.AddField(
            model_name="postagesettings",
            name="express_delivery",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Cost of express delivery - % of TOTAL",
                max_digits=5,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="postagesettings",
            name="standard_delivery",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Cost of standard delivery - % of TOTAL",
                max_digits=5,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="postagesettings",
            name="free_postage",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Amount in € that TOTAL needs to be over for free delivery",
                max_digits=5,
            ),
        ),
    ]
