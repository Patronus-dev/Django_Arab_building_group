from django.urls import path
from django.conf.urls import handler404

from .views import *

custom_page_not_found_view = handler404

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),

]
