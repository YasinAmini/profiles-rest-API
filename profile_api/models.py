from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def creat_user(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        email=self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password) #set_password function will encrypt the databases
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given detail"""
        user=self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Databse model for users in the system""" #Doc string
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_fIELDS= ['name']


    def get_full_name (sels):
        """Retrive fullname of user"""
        return self.name

    def get_short_name(sels):
        """Retrive the short name"""
        return self.name

    def __str__(self):
        """return string representation of the our user"""
        return self.email



# Create your models here.