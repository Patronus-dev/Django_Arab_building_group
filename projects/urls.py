from django.urls import path

from .views import ProjectListView, ProjectDetailView

app_name = 'project'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

]
