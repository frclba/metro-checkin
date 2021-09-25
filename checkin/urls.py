# checkin/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from checkin import views

urlpatterns = [
    path('checkin/record', views.RecordList.as_view()),
    path('checkin/record/<int:pk>/', views.RecordDetail.as_view()),
    path('checkin/swipe_in/', views.SwipeIn.as_view()),
    path('checkin/swipe_out/', views.SwipeOut.as_view()),
    path('checkin/avg_travel_time/', views.AvgTravelTime.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)