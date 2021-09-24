import datetime
from time import time
from rest_framework import generics
from .models import Rider, Station, Timesheet
from .serializers import RiderSerializer, StationSerializer, TimesheetSerializer
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

        station_obj = Station.objects.filter(station_id=filtered_station_id)[0]
        rider_obj = Rider.objects.filter(user_id=fitered_user_id)[0]
        
        newEntry = Timesheet(
            user_id=rider_obj,
            station_id=station_obj,
            entry_type="swipe_in",
            created=datetime.datetime.utcnow()
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

        station_obj = Station.objects.filter(station_id=filtered_station_id)[0]
        rider_obj = Rider.objects.filter(user_id=fitered_user_id)[0]
        
        newEntry = Timesheet(
            user_id=rider_obj,
            station_id=station_obj,
            entry_type="swipe_out",
            created=datetime.datetime.utcnow()
        )

        newEntry.save()
        return Response('created')


class AvgTravelTime(generics.ListCreateAPIView):
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer
    
    def post(self, request, *args, **kwargs):
        print(request)
        swipeInsFromFirstReqStation = Timesheet.objects.get(
            request[0]).filter(type="swipe_in")
        swipeOutsFromSecondReqStation = Timesheet.objects.get(
            request[1]).filter(type="swipe_out")

        datetimeList = swipeInsFromFirstReqStation + \
            swipeOutsFromSecondReqStation

        avgTime = datetime.datetime.strftime(datetime.datetime.fromtimestamp(sum(
            map(datetime.datetime.timestamp, datetimeList))/len(datetimeList)), "%H:%M:%S")

        return Response('avgTime')
