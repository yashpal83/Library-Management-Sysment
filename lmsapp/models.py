from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('Email address', unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.email

class Book(models.Model):
    sno = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    quantity = models.CharField(max_length=10)

    def __str__(self):
        return self.book_name 


