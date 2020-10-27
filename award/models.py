# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

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
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_project(self):
        self.save()

    @classmethod
    def save_project(cls):
        projects=cls.objects.filter()
        return projects
    
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    def update_project(self):
        self.update()

    def delete_project():
        self.delete()

