from django.db import models

# Create your models here.
class Marvel(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)