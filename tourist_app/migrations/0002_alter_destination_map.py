# Generated by Django 4.1.5 on 2024-06-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='map',
            field=models.URLField(),
        ),
    ]
