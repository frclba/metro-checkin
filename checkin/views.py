from datetime import datetime
from time import time
from rest_framework import generics
from .models import Rider, Station, Timesheet
from .serializers import RiderSerializer, StationSerializer, TimesheetSerializer, AvgTravelTimeSerializer
from rest_framework.response import Response


class RiderList(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer


class RiderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer


class StationList(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class TimesheetList(generics.ListCreateAPIView):
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer


class TimesheetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer


class SwipeIn(generics.ListCreateAPIView):
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        if data['station_id'].find('S') == 0:
            filtered_station_id = int(data['station_id'].replace('S', ''))
        else:
            filtered_station_id = data['station_id']

        if data['user_id'].find('U') == 0:
            fitered_user_id = int(data['user_id'].replace('U', ''))
        else:
            fitered_user_id = data['user_id']

        station_obj = Station.objects.filter(station_id=filtered_station_id)[0]
        rider_obj = Rider.objects.filter(user_id=fitered_user_id)[0]

        if data['time_stamp'].find('-') == 0:
            datestring = "%M-%D-%Y %H:%M"
        else:
            datestring = "%H:%M"

        created_time = datetime.strptime(data['time_stamp'], datestring)

        newEntry = Timesheet(
            user_id=rider_obj,
            station_id=station_obj,
            entry_type="swipe_in",
            created=created_time
        )

        newEntry.save()
        return Response('created')


class SwipeOut(generics.ListCreateAPIView):
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer

    def post(self, request):
        data = request.data

        if data['station_id'].find('S') == 0:
            filtered_station_id = int(data['station_id'].replace('S', ''))
        else:
            filtered_station_id = data['station_id']

        if data['user_id'].find('U') == 0:
            fitered_user_id = int(data['user_id'].replace('U', ''))
        else:
            fitered_user_id = data['user_id']

        timestamp = ''
        if(data['time_stamp']):
            timestamp = data['time_stamp']
        else:
            timestamp = data['created']

        datestring = ''
        if timestamp.find('-') == 0:
            datestring = "%M-%D-%Y %H:%M"
        else:
            datestring = "%H:%M"

        station_obj = Station.objects.filter(station_id=filtered_station_id)[0]
        rider_obj = Rider.objects.filter(user_id=fitered_user_id)[0]

        created_time = datetime.strptime(data['time_stamp'], datestring)

        newEntry = Timesheet(
            user_id=rider_obj,
            station_id=station_obj,
            entry_type="swipe_out",
            created=created_time
        )

        newEntry.save()
        return Response('created')


class AvgTravelTime(generics.ListCreateAPIView):
    queryset = Timesheet.objects.all()
    serializer_class = AvgTravelTimeSerializer

    def post(self, request, *args, **kwargs):

        if request.data['start_station_id'].find('S') == 0:
            filtered_start_station_id = int(
                request.data['start_station_id'].replace('S', ''))
        else:
            filtered_start_station_id = request.data['start_station_id']

        if request.data['end_station_id'].find('S') == 0:
            filtered_end_station_id = int(
                request.data['end_station_id'].replace('S', ''))
        else:
            filtered_end_station_id = request.data['end_station_id']

        swipeInsFromFirstReqStation = Timesheet.objects.filter(
            station_id=filtered_start_station_id).filter(entry_type="swipe_in")

        swipeOutsFromSecondReqStation = Timesheet.objects.filter(
            station_id=filtered_end_station_id).filter(entry_type="swipe_out")

        datetimeList = []
        for item in swipeInsFromFirstReqStation:
            datetimeList.append(item.created)
        for item in swipeOutsFromSecondReqStation:
            datetimeList.append(item.created)

        avgTime = datetime.strftime(datetime.fromtimestamp(sum(
            map(datetime.timestamp, datetimeList))/len(datetimeList)), "%H:%M:%S")

        return Response(avgTime)
