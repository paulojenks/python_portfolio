from django.db import models
from tinymce.models import HTMLField


class Entry(models.Model):
    author = models.CharField(max_length=144)
    title = models.CharField(max_length=144)
    content = HTMLField('content')
    date_published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "entries"
        ordering = ['date_published']
