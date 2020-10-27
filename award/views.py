# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, Project
from .forms import NewProjectForm, UpdateProfile, UpdateUser

# Create your views here.
@login_required(login_url='/accounts/login/')
def project(request):
    profile=Profile.objects.all()
    projects=Project.objects.all()
    return render(request, 'project.html',{"profile":profile, "projects":projects})

def profile(request):
    profile=Profile.objects.all()
    projects=Project.objects.all()
    return render(request, 'profile.html',{"profile":profile, "projects":projects})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('project')
        
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form":form, "current_user":current_user})

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        update_user=UpdateUser(request.POST,instance=request.user)
        update_profile=UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
    if update_user.is_valid() and update_profile.is_valid():
        update_user.save()
        update_profile.save()
        return redirect('profile')
    else:
        update_user=UpdateUser(instance=request.user)
        update_profile=UpdateProfile(instance=request.user.profile)
    return render(request, 'update_profile.html',{'update_user':update_user,'update_profile':update_profile})

#