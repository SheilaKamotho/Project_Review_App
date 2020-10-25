# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.TextField()
    contact = models.TextField()

    def save_profile(self):
        self.save()

    @classmethod
    def save_profile(cls):
        posts=cls.objects.filter()
        return posts

    def update_profile(self):
        self.update()

    def delete_profile():
        self.delete()


