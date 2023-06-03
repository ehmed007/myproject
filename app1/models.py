from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=1000, null=False)
    date = models.DateField()
    time = models.TimeField()
    poster = models.ImageField(upload_to='posters')
    duration =  models.DurationField()