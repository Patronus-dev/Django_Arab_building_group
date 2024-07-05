from django.urls import path
from .views import *

urlpatterns = [
    path('materials/', MaterialListView.as_view(), name='material'),

]
