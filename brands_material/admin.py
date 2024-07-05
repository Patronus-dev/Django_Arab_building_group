from django.contrib import admin
from .models import BrandMaterial, Category


@admin.register(BrandMaterial)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime_created')
    ordering = ('datetime_created', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'active', )
