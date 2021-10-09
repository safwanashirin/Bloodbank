from django.db import models

# Create your models here.
class database(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=20)
