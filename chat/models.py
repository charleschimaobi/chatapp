from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    content = models.CharField(max_length=1000000)
    sender = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)