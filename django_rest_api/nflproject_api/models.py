from django.db import models

# Create your models here.

class Teams(models.Model):
    name = models.CharField(max_length=32)
    players = models.TextField()

