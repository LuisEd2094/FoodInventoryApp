from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return (self.name)
    
class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    houses = models.ManyToManyField(House)
    