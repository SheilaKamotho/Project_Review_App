# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, Project
# Create your views here.
@login_required(login_url='/accounts/login/')
def project(request):
    profile=Profile.objects.all()
    project=Project.objects.all()
    return render(request, 'project.html',{"profile":profile, "project":project})

