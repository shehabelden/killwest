from django.contrib.auth.models import User
from django.db import models

class EventModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, default="s")
    image = models.ImageField()
    bio = models.CharField(max_length=4000)
    date = models.DateField(auto_now=True)
    start = models.DateField(auto_now=True)
    end = models.DateField(auto_now=True)
    avilabolevent = models.BooleanField(default=True)
