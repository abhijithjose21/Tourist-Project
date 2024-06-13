from django.db import models


# Create your models here.


class Destination(models.Model):
    Name = models.CharField(max_length=255)
    Weather = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    dist = models.CharField(max_length=255)
    map = models.URLField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.Name
