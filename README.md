# Requirements

Imagine a subway train system where riders have to swipe to enter a station, and swipe to exit a station when they leave. In this system, every rider has an integer user_id and every station has an integer station_id. 

The goal is to create a system to track when riders enter and leave stations, and provide the average travel time between subway stations, through the following REST API’s:
- POST for swipe in, given user_id and station_id and time_stamp
- POST for swipe out, given user_id and station_id and time_stamp
- GET average time, given start_station_id, and end_station_id.
- the return value can either be a time duration format of HH:MM:SS, or just an integer for minutes

Please develop a Django webserver that supports the functionality above, deploy it anywhere that you like (aws, google cloud, heroku, etc), and provide:
- the server url to send requests to. 
- the url to the repo (github/gitlab/etc)

Please let us know if you have any questions that we can help clarify!



Example: One subway ride for 20m, and another for 10m, averages to 15m
POST swipe_in (U1, S1, 11:00)
POST swipe_out (U1, S3, 11:20) 
POST swipe_in (U2, S1, 11:30)
POST swipe_out (U2, S3, 11:40)
GET avg_trave_time(S1, S2) -> should return 15m 

