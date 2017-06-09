from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Photo(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    photo_title = models.CharField(max_length=100)
    photo_pic = models.FileField()

    def get_absolute_url(self):
        return reverse('simplegram:index')

    def __str__(self):
        return self.photo_title
