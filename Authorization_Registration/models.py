from django.db import models

# Create your models here.
class Auth(models.Model):
    phone=models.IntegerField()
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    login=models.CharField(max_length=255)