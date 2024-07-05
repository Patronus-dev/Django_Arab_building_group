from django import template
from blog.views import BlogDetailView

register = template.Library()


@register.simple_tag
def get_blog_detail_context(blog_id):
    view = BlogDetailView()
    request = None
    view.request = request
    view.kwargs = {'pk': blog_id}
    view.get(request, pk=blog_id)
    context = view.get_context_data()
    return context
