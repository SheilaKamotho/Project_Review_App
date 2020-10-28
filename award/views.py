# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http  import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Review
from .serializer import ProfileSerializer, ProjectSerializer
from .forms import NewProjectForm, UpdateProfile, UpdateUser, RateForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def project(request):
    profile=Profile.objects.all()
    projects=Project.objects.all()
    return render(request, 'project.html',{"profile":profile, "projects":projects})

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    print(profile)
    update_user=UpdateUser(request.POST,instance=request.user)
    update_profile=UpdateProfile(request.POST,request.FILES,instance=profile)
    if update_user.is_valid() and update_profile.is_valid():
        update_user.save()
        update_profile.save()
        return redirect('profile')
    else:
        update_user=UpdateUser(instance=request.user)
        update_profile=UpdateProfile(instance=profile)
    return render(request, 'update_profile.html',{'update_user':update_user,'update_profile':update_profile})

@login_required(login_url='/accounts/login/')
def rate(request):
    project = Project.objects.get(request.user.project)
    user = request.user

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.movie = movie
            rate.save()
            return HttpResponseRedirect(reverse('profile', args=[project_id]))

        else:
            form = RateForm()
            template = loader.get_template('rate.html')
            context = {
            'form':form,
            'project': project,
            }

        return HttpResponse(template.render(context, request))

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

    