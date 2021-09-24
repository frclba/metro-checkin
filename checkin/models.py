# checkin/models.py
from django.db import models
from datetime import timedelta

class Rider(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    user_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.user_id) + " - " + self.name


class Station(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    station_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.station_id) + " - " + self.name + " " + self.location


class Timesheet(models.Model):
    user_id = models.ForeignKey(Rider, on_delete=models.CASCADE)
    station_id = models.ForeignKey(Station,on_delete=models.CASCADE)
    entry_type = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'user: ' + str(self.user_id) + ' station ' + str(self.station_id) + ' type: ' + self.entry_type + ' when: ' + str(self.created)

class AvgTravelTime(models.Model):
    station_id = models.ManyToManyField(Station)