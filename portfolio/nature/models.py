from django.db import models

# Create your models here.
class trees(models.Model):
    subject = models.CharField(max_length = 100)
    body = models.TextField(max_length = 100)
    tittle = models.CharField(max_length = 100)