from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from mypage.models import Profile
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,profile_id,password = None,**extra_fields):
        if not email:
            raise ValueError('Users must have a email address')
        if not first_name:
            raise ValueError('User must have a first_name')
        if not last_name:
            raise ValueError('User must have a last_name')
        email = MyUserManager.normalize_email(email)
        user = self.model(email = email,first_name = first_name,last_name=last_name,profile_id=profile_id,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,email,first_name,last_name,password):
        return self.create_user(email,first_name,last_name,password)

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=128,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE,)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    objects = MyUserManager()
    # class Meta:
        # swappable = 'AUTH_USER_MODEL'
    def validate_unique(self, exclude=None):
        """Validate the field uniqueness"""
        MyUser.objects.filter(email=self.email, is_active=False).delete()
        super(MyUser, self).validate_unique(exclude)
