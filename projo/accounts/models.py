from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_info):
        if not email:
            raise ValueError("Email ID is required!")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_info)
        user.set_password(password)
        user.save()
        return user
    
    def create_super_user(self, email, password=None, **extra_info):
        extra_info.setdefault('is_staff', True)
        extra_info.setdefault('is_superuser', True)
        
        if extra_info.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff=True')
        if extra_info.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser=True')
        
        return self.create_user(email, password, **extra_info)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    joining_date = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
