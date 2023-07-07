from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images')


class Data(models.Model):
    date = models.DateField()
