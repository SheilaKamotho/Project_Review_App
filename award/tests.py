# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
# Create your tests here.
class ProfileClass(TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_profile=Profile(bio = 'Sheila is becoming a world class software developer')

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_update_method(self):
        self.new_profile.save_profile()
        self.new_profile= Profile.objects.filter(id==1).update()
        self.updated_profile=Profile.objects.get(id==1)
        self.assertTrue(self.updated_profile.img,'posts')

    def test_profile_delete(self):
        self.profile.save_profile()
        self.searched_profile = Profile.objects.get(id==1)
        self.searched_profile.delete_profile()
        self.assertTrue(len(Profile.objects.all()) == 0)

class ProjectClass(TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_profile=Profile(bio='World Class Software Developer',contact='kamothosheila@gmail.com')
        self.new_profile.save_profile()

        self.new_project=Project(title='InstaApp',description='instagram clone',link='insta.com')
        self.new_project.save

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_project.save()
        project=Project.objects.all()
        self.assertTrue(len(project)>0)

    def test_project_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def test_project_update(self):
       self.project.save_project()
       self.project=Project.objects.filter(id==1).update() 
       self.updated_project=Project.objects.get(id==1)
       self.assertTrue(self.updated_project.img,'projects')


    def test_project_delete(self):
        self.project.save_project()
        self.searched_project = Project.objects.get(id==1)
        self.searched_project.delete_project()
        self.assertTrue(len(Project.objects.all()) == 0)

    def test_search_project_category(self):
        self.project.save_project()
        self.title= Title(title='InstaApp')
        self.name.save_name()
        self.searched_project=Project.search_by_title('InstaApp')
        self.assertTrue(len(self.searched_projects) > 0)