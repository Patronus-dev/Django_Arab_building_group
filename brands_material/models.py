from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class BrandMaterial(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100, blank=False)
    datetime_created = models.DateTimeField(verbose_name=_('date created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(verbose_name=_('date edited'), auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_('Brand Image'), upload_to='Brand_materials/brand_cover/', blank=False)

    def __str__(self):
        return self.title
