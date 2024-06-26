from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfilesManager(BaseUserManager):
    """Manager for user profile"""
    def create_user(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("user must have an email address")
        email=self.normalize_email(email
                                   )
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """create and save a new superuser with given details"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        
        return user

# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfilesManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]

    def get_full_name(self):
        """retreive full name of user"""
        return self.name
    def get_short_name(self):
        """retreive short name of user"""
        return self.name
    
    def __str__(self) :
        """return string representation of our user"""
        return self.email
        