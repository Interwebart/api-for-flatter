from django.db import models
from datetime import datetime, date


class Car(models.Model):
    vendor = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    volume = models.PositiveIntegerField()


class Fighter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth= models.DateTimeField()
    age = models.PositiveSmallIntegerField(default=0)
    weight = models.FloatField()
    growth = models.FloatField()
