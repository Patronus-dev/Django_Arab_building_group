from django.shortcuts import render, redirect
from django.views.generic import *

from .models import Project, ProjectPhoto


class ProjectListView(ListView):
    queryset = Project.objects.filter(active=True)
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_gallery'] = ProjectPhoto.objects.filter(project=self.object)
        return context
