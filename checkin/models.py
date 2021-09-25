# checkin/models.py
from django.db import models


class Record(models.Model):
    user_id = models.CharField(max_length=256, blank=False)
    station_id = models.CharField(max_length=256, blank=False)
    action = models.CharField(max_length=64)  # swipe_in, swipe_out
    datetime = models.DateTimeField(blank=False)


class AvarageTravelTime(models.Model):
    start_station_id = models.CharField(max_length=256, blank=False)
    end_station_id = models.CharField(max_length=64)  # swipe_in, swipe_out
