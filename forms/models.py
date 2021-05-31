import forms
from django.db import models

# Create your models here.
class Basic_model(models.Model):
    name = models.CharField( max_length=255)
    email = models.CharField(max_length=255)
    text = models.TextField()