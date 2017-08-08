from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class CommonUser(User):
    pass

class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']
        

# Create your models here.
