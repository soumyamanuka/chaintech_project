from django.db import models

# Create your models here.
class Data(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
