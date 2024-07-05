from django.shortcuts import render
from django.views import generic

from .models import BrandMaterial


class MaterialListView(generic.ListView):
        model = BrandMaterial
        template_name = 'brands_material/material_list.html'
        context_object_name = 'materials'
