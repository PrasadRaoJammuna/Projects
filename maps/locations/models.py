from django.db import models

# Create your models here.

from django.contrib.gis.db.models import PointField
from django.db.models import Manager as GeoManager


class City(models.Model):
    name = models.CharField(max_length=100)
    coords = PointField(srid=4326)
    temperature = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    objects = GeoManager()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'