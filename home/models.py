from unicodedata import name
from django.db import models
from django.forms import PasswordInput



# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    desc = models.TextField()
    timestamp = models.DateField(auto_now_add=True,blank=True)


    def __str__(self):
        return self.name

