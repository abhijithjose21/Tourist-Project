# Generated by Django 4.1.5 on 2024-06-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0004_rename_dest_destination_dist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='Weather',
        ),
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='destination',
            name='dist',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='state',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='destination',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='weather',
            field=models.CharField(default=1234, max_length=255),
            preserve_default=False,
        ),
    ]
