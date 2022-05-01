import modulefinder

from django.db import models
from django.contrib.auth.models import User
import uuid
from PIL import Image
import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver



# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    featured_image = models.ImageField(null=True,blank=True, default="images/images/default.jpg", upload_to="images/userupload")
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200,blank= True, null=True)
    tags = models.ManyToManyField('Tag',blank= True)
    detail = models.TextField(null=True, blank=True)
    source_link = models.URLField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # def save(self, *args, **kwargs):
    #     instance = super(Recipe, self).save(*args, **kwargs)
    #     img = Image.open(instance.featured_image.path)
    #     img.save(instance.featured_image.path, quality=20, optimize=True)
    #     return instance

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Material(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length= 20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.name

class Sauce(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    # unit = models.CharField(max_length= 20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

#沒使用到
class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete= models.CASCADE)
    image = models.ImageField(null=True,blank=True, default="images/default.jpg", upload_to="images/userupload")

