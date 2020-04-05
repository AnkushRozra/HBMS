from django.db import models
from Hotels.City import *
from Hotels.star_rating import *

# Create your models here.
class Hotels(models.Model):
    id       = models.IntegerField(primary_key=True)
    name     = models.CharField(max_length=120)
    location = models.IntegerField(choices=city_choice)
    email    = models.EmailField(null=True)
    star     = models.IntegerField(choices=Star_rating)
