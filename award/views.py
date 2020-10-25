# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render
from django.http  import HttpResponse

# Create your views here.
def project(request):
    return render(request, 'project.html')