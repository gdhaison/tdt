from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False, unique=True)
    adress = models.CharField(max_length=200)
    age = models.IntegerField()
