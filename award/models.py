# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.TextField()
    contact = models.TextField()

    def save_profile(self):
        self.save()

    @classmethod
    def save_profile(cls):
        profile=cls.objects.filter()
        return profile

    def update_profile(self):
        self.update()

    def delete_profile():
        self.delete()

class Project(models.Model):
    title = models.CharField(max_length = 60)
    image = models.ImageField(upload_to = 'image/')
    description = models.TextField()
    link = models.CharField(max_length = 300)
    def save_project(self):
        self.save()

    @classmethod
    def save_project(cls):
        project=cls.objects.filter()
        return project
    
    def search_by_title(cls,search_term):
        proj = cls.objects.filter(title__icontains=search_term)
        return proj

    def update_project(self):
        self.update()

    def delete_project():
        self.delete()