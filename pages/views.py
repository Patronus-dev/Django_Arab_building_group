from django.shortcuts import render
from django.views.generic import TemplateView

from projects.models import Project
from blog.models import Blog


class HomePageView(TemplateView):
    template_name = 'home.html'

    #  in this part , we can access to Values of app.models from home page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_projects'] = Project.objects.all().order_by('-id')
        context['all_blogs'] = Blog.objects.all().order_by('-id')
        return context


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'
