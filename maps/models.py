from django.db import models

# Create your models here.
class Coordinate(models.Model):
    date = models.DateTimeField('Date')
    longitude = models.FloatField()
    latitude = models.FloatField()