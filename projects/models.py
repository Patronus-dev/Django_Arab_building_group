from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    BUILDING_STATUS = [
        ('done', _('Done!')),
        ('building', _('Building...')),
    ]

    title = models.CharField(max_length=50, blank=False, verbose_name=_('Title'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    status = models.CharField(max_length=20, choices=BUILDING_STATUS, verbose_name=_('Status'))
    description = models.TextField(max_length=700, blank=False, verbose_name=_('description'))
    ground_meterage = models.FloatField(default=0, blank=True, null=True, verbose_name=_('ground meterage'))  # meterage of ground
    address = models.TextField(max_length=100, blank=False, verbose_name=_('address'))

    date_construction = models.IntegerField(default=timezone.now().year, blank=True, null=True, verbose_name=_('date construction'))  # shows the year of construction by default
    plus_floor = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('floors'))  # Number of all floors
    minus_floor = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('floors underground'))  # Number of floors underground
    units = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('units'))  # Number of all units
    units_in_floor = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('units in each floor'))  # Number of units in each floor
    unit_meterage = models.FloatField(default=0, blank=True, null=True, verbose_name=_('meterage'))  # meterage of each unit
    room = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Rooms'))  # Number of rooms
    image_cover = models.ImageField(upload_to='project/project_cover/', blank=True, null=True, verbose_name=_('image'))

    def __str__(self):
        return self.title

    def __iter__(self):
        return iter(self.projectphoto_set.all())


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image_gallery = models.ImageField(upload_to='project/project_photos/', blank=True, null=True)

    def __str__(self):
        return f"Photo of {self.project.title}"
