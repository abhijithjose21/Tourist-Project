# Generated by Django 4.1.5 on 2024-06-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Weather', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('dest', models.CharField(max_length=250)),
                ('map', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='palce')),
                ('desc', models.CharField(max_length=5000)),
            ],
        ),
    ]
