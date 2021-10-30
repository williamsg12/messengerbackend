from django.db import models
from django.db.models.deletion import CASCADE
from user.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('O', 'Other',),
    )
    username=models.CharField(max_length=20, default=None)
    name=models.CharField(max_length=20)
    age = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(255)])
    account_owner=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,default=None)

    def __str__(self):
        return self.name
