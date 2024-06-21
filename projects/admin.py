from django.contrib import admin
from .models import Project, ProjectPhoto


class ProjectPhotosInline(admin.TabularInline):
    model = ProjectPhoto
    extra = 10


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'status', )
    inlines = [ProjectPhotosInline]
