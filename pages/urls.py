from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),

]
