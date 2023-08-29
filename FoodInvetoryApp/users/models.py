from django.db import models
from django.contrib.auth.models import AbstractUser
from house.models import House

# Create your models here.
class User(AbstractUser):
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.username