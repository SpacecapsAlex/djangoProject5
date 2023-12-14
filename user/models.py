from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(22)
    email = models.EmailField()