from pyexpat import model
from django.db import models

# Create your models here.
class TestOne(models.Model):
    title = models.CharField(max_length=100)
    cpu = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    motherboard =models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_created=True) 