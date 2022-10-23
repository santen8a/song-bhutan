from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    artist = models.CharField(max_length=255)
    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255,default='general')
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
       return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic =models.ImageField(null=True,blank=True,upload_to="images/profile/") 
    website_url = models.CharField(max_length=255,null=True)
    twitter_url = models.CharField(max_length=255,null=True)
    linkedin_url = models.CharField(max_length=255,null=True) 

    def __str__(self):
        return str(self.user)