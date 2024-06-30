from django.shortcuts import render
from django.views import generic

from .models import Blog


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
