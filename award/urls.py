from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.project, name='project'),
]