# checkin/models.py
from django.db import models

class Rider(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    user_id = models.IntegerField() # TODO => add unique key and other params
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.user_id


class Station(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    station_id = models.IntegerField() # TODO => add unique key and other params

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.station_id