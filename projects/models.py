from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False)
    active = models.BooleanField(default=True)
    description = models.TextField(max_length=200, blank=False)
    address = models.TextField(max_length=100, blank=False)

    date_construction = models.IntegerField(default=timezone.now().year, blank=True, null=True)  # shows the year of construction by default
    plus_floor = models.IntegerField(default=0, blank=True, null=True)  # Number of floors on ground
    minus_floor = models.IntegerField(default=0, blank=True, null=True)  # Number of floors underground
    units = models.IntegerField(default=0, blank=True, null=True)  # Number of all units
    units_in_floor = models.IntegerField(default=0, blank=True, null=True)  # Number of units in each floor
    unit_meterage = models.FloatField(default=0, blank=True, null=True)  # meterage of each unit
    image = models.ImageField(upload_to='project/project_cover/', blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/project_photos/', blank=True, null=True)

    def __str__(self):
        return self.project
