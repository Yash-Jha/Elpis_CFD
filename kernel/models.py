from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)

class City(models.Model):
    name = models.CharField(max_length=16)
    lat = models.FloatField()
    lng = models.FloatField()

class Year(models.Model):
    year = models.IntegerField()
    density = models.FloatField()
