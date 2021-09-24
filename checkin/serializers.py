from rest_framework import serializers
from .models import Rider, Station, Timesheet


class RiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rider
        fields = ('user_id', 'name')


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('station_id', 'name', 'location')


class TimesheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timesheet
        fields = ('user_id', 'station_id', 'entry_type', 'created')