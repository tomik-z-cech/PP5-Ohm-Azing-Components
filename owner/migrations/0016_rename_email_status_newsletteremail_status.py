# Generated by Django 4.2.7 on 2024-02-25 12:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("owner", "0015_rename_status_newsletteremail_email_status_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newsletteremail",
            old_name="email_status",
            new_name="status",
        ),
    ]
