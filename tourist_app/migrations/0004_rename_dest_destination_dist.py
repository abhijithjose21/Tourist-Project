# Generated by Django 4.1.5 on 2024-06-08 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0003_alter_destination_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='dest',
            new_name='dist',
        ),
    ]
