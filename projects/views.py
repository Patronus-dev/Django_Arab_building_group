from django.shortcuts import render, redirect
from django.views.generic import *

from .models import Project


class ProjectListView(ListView):
    # model = Product
    queryset = Project.objects.filter(active=True)
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
