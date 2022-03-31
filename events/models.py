from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    description =RichTextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank = True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank = True)
    icons = models.ImageField(upload_to='photos/%Y/%m/%d/', blank = True)
    is_featured = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name