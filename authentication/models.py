from django.db import models
from django.contrib.auth.models import UserManager,AbstractUser, AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone


# Create your models here.
class CustomUserManger(BaseUserManager):
    def create_user(self,username,email,phonenumber,idnumber,password=None):
        if username is None:
            raise TypeError("Users should have a username")
        if email is None:
            raise TypeError("Users should have an email")
        if phonenumber is None:
            raise TypeError("users should have a phonenumber")
        if idnumber is None:
            raise TypeError("users should have an idnumber")
        email = self.normalize_email(email)
        user=self.model(username=username,email=email,phonenumber=phonenumber,idnumber=idnumber) #self.normalize_email)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self,username,email,password=None):
        user=self.model(username=username,email=email) #self.normalize_email)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255,unique=True,db_index=True,default='')
    email = models.EmailField(max_length=255,db_index=True,default='')
    phonenumber=models.DecimalField(max_digits=10,decimal_places=0,max_length=255,default=0)
    idnumber=models.DecimalField(max_digits=15,decimal_places=0,max_length=255,primary_key=True,db_index=True,default=0)
    is_verified = models.BooleanField(default = True)
    is_active= models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =['email' ]

    objects = CustomUserManger()

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username or self.email.split('@')[0]
    
    def __str__(self):
        return self.email
    