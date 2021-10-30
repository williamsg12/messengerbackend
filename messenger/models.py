from typing import Text
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

from user.models import User


# Create your models here.

class Post(models.Model):
    picture=models.ImageField(upload_to='image', blank=True)
    body= models.TextField(max_length=250)
    owner=models.ForeignKey('user.User',on_delete=CASCADE,null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    
    
