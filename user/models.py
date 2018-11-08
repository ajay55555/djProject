from django.db import models

# Create your models here.

class register(models.Model):
    userName = models.CharField(max_length=250, blank=True)

