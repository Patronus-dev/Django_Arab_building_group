from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse


class Blog(models.Model):
    STATUS_CHOICES = (
        ('pub', _('published')),
        ('drf', _('draft'))
    )

    title = models.CharField(verbose_name=_('Title'), max_length=100, blank=False)
    author = models.CharField(verbose_name=_('Author'), max_length=50, blank=False)
    text = models.TextField(verbose_name=_('Text'), max_length=1000)
    datetime_created = models.DateTimeField(verbose_name=_('date created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(verbose_name=_('date edited'), auto_now=True)
    image = models.ImageField(verbose_name=_('blog Image'), upload_to='blog/blog_cover/', blank=True)
    status = models.CharField(verbose_name=_('Status'), choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return f'{self.title} - {self.author}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
