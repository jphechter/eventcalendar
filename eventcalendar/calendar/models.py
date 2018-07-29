from django.db import models

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0, null=False, blank=False)

class Event(models.Model):
    name = models.CharField(max_length=255, blank=False, default="")
    pub_date = models.DateTimeField('date published')
    event_date = models.DateTimeField('event date')
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)