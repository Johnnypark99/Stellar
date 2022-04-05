from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os


# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='files/')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return os.path.split(self.file.name)[1]
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
