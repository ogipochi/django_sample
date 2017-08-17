from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    nickname = models.CharField(max_length=50,blank=True,default="")
    favorite_musician = models.TextField(max_length=300,blank=True,default="")
    my_inst = models.TextField(max_length=300,blank=True,default="")

