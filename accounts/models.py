from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.


class CustomAccountMangager(BaseUserManager):

    def create_superuser(self,email,user_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Super users must be staff')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Super users must be set to True')

        
        return self.create_user(email,user_name,password,**other_fields)

    def create_user(self,email,user_name,password,**other_fields):

        if not email:
            raise ValueError('you must provide email to register')

        email= self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,**other_fields)
        user.set_password = (password)
        user.is_admin = True
        user.save()
        print(user)
        return user


class UserBase(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    user_name = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountMangager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    class Meta:
        verbose_name ='Accounts'
        verbose_name_plural = 'Accounts'
    def __str__(self):
        return self.user_name
