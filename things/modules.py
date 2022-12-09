# Exercise 2 + 3

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from enum import unique



class Thing(models.Model):
    name = models.CharField(max_length=30, unique = True, blank = False)
    description = models.CharField(max_length =120, blank =True)
    quantity = models.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(100)] )
