from statistics import mean
from .models import Record
from datetime import datetime
from rest_framework import generics
from .models import Record, AvarageTravelTime
from .serializers import RecordSerializer, AvarageTravelTimeSerializer
from rest_framework.response import Response


class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class SwipeIn(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def post(self, request):
        '''
            POST for swipe in, given user_id and station_id and time_stamp
        '''
        user_id = request.POST.get('user_id')
        station_id = request.POST.get('station_id')
        all_records = Record.objects.all()
        action = 'swipe_in'
        timestamp = datetime.strptime(request.POST.get(
            'datetime'), '%Y-%m-%dT%H:%M').replace(tzinfo=None)

        last_record = all_records.filter(user_id=user_id).last()

        if last_record and last_record.action != "swipe_out":
            return Response('Please swipe out first')
        if last_record and last_record.datetime.replace(tzinfo=None) >= timestamp:
            return Response("Can't swipe_in in past")

        record = Record(user_id=user_id, station_id=station_id,
                        action=action, datetime=timestamp)

        record.save()

        return Response("Request done !!")


class SwipeOut(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def post(self, request):
        '''
            POST for swipe out, given user_id and station_id and time_stamp
        '''
        user_id = request.POST.get('user_id')
        station_id = request.POST.get('station_id')
        action = 'swipe_out'
        timestamp = datetime.strptime(request.POST.get(
            'datetime'), '%Y-%m-%dT%H:%M').replace(tzinfo=None)

        all_records = Record.objects.all()
        last_record = all_records.filter(user_id=user_id).last()

        if last_record is None:
            return Response('Please swipe in first')
        if last_record.action != "swipe_in":
            return Response('Please swipe in first')
        if last_record.datetime.replace(tzinfo=None) >= timestamp:
            return Response("Can't swipe_out in past")
        if last_record.station_id == station_id:
            return Response('Cannot swipe out at the same station you swiped in')

        record = Record(user_id=user_id, station_id=station_id,
                        action=action, datetime=timestamp)

        record.save()

        return Response("Request done !!")


class AvgTravelTime(generics.ListCreateAPIView):
    queryset =  AvarageTravelTime.objects.all()
    serializer_class = AvarageTravelTimeSerializer

    def post(self, request):
        start_station = request.data['start_station_id']
        end_station = request.data['end_station_id']
        
        print(start_station, end_station)

        travel_times = []
        for swipe_in in Record.objects.filter(station_id=start_station, action='swipe_in'):
            swipe_out = get_swipe_out(swipe_in)
            if swipe_out is not None and swipe_out.station_id == end_station:
                travel_times.append(
                    (swipe_out.datetime - swipe_in.datetime).seconds/60)

        if travel_times == []:
            return Response('No journeys has been completed between these stations so far')
        return Response(str(round(mean(travel_times), 2)))


def get_swipe_out(swipe_in):
    user_swipe_out = Record.objects.filter(
        user_id=swipe_in.user_id, action='swipe_out', datetime__gt=swipe_in.datetime).first()
    return user_swipe_out
