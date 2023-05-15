from django.db import models

# Create your models here.

class PredictResult(models.Model):
    name = models.CharField(max_length=20, null=False)
    image = models.ImageField(null=False, blank=False)
    result = models.CharField(max_length=8)

class MapLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.date
