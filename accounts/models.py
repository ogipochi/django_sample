from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.utils import timezone
import re
from django.core.mail import send_mail
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,email,password,**extra_fields):
        # ログイン時間を始めに記録するための時間
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address.')
        # ドメイン部分を小文字化しメールアドレスを標準化する
        email = UserManager.normalize_email(email)
        user = self.model(
            username = username,
            email = email,
            is_active = True,
            last_login = now,
            date_joined = now,
            **extra_fields
        )
        # パスワードのハッシュ値をpasswordに記録
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password,**extra_fields):
        user = self.create_user((username,email,password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    username    = models.CharField(_('username'),max_length=30)
    first_name = models.CharField(_('first name'),max_length=30,blank=False)
    last_name = models.CharField(_('last name'),max_length=30,blank=False)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,blank=False)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'),default=timezone.now)
    delete = models.BooleanField(default=0)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def email_user(self,subject,message,from_email=None):
        # このユーザにメールを送信
        send_mail(self,subject,message,from_email,[self.email])
    
    # スーパーユーザかどうかのgetter
    @property
    def is_superuser(self):
        return self.is_admin
    


