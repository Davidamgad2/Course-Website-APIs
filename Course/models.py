from random import choices
from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Course(models.Model):
    """Hnadling courses model"""
    name = models.CharField(max_length=300)
    reviews = models.ManyToManyField('Review')
    price = models.IntegerField()
    includes = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Courses images')
    description = models.TextField()
    overview = models.TextField()
    instructor = models.ManyToManyField('Instructor')
    language = models.CharField(max_length=30)
    rate = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    date = models.DateTimeField()


class Instructor(models.Model):
    """Handling instructor model"""
    name = models.CharField(max_length=300)
    description=models.TextField()
    number=models.IntegerField()
    courses=models.TextField() #hna al mfrod a5od al courses ali ll ragl dh


class Review(models.Model):
    """Handling Reviews model"""
    name=models.CharField(max_length=300) #hna al mfrod a5od asm al user ali hy3ml al review
    comment=models.TextField()
    rate = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
