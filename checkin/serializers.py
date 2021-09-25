from rest_framework import serializers
from .models import AvarageTravelTime, Record


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('user_id', 'station_id', 'action', 'datetime')


class AvarageTravelTimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AvarageTravelTime
        fields = ('start_station_id', 'end_station_id')
