from django import forms
from .models import Profile, Project
from django.contrib.auth.models import User

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']