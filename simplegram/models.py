from django.db import models
from django.utils import timezone

class Photo(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    photo_title = models.CharField(max_length=100)
    photo_pic = models.FileField()

    def __str__(self):
        return self.photo_title
