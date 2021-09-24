# checkin/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from checkin import views

urlpatterns = [
    path('checkin/rider', views.RiderList.as_view()),
    path('checkin/rider/<int:pk>/', views.RiderDetail.as_view()),
    path('checkin/station/', views.StationList.as_view()),
    path('checkin/station/<int:pk>/', views.StationDetail.as_view()),
    path('checkin/timesheet/', views.TimesheetList.as_view()),
    path('checkin/timeshet/<int:pk>/', views.TimesheetDetail.as_view()),
    path('checkin/swipe_in/', views.SwipeIn.as_view()),
    path('checkin/swipe_out/', views.SwipeOut.as_view()),
    path('checkin/avg_travel_time/', views.AvgTravelTime.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)