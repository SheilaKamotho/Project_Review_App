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

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})