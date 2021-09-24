from django.contrib import admin
from .models import Rider, Timesheet, Station

# Register your models here.
admin.site.register(Rider)
admin.site.register(Timesheet)
admin.site.register(Station)

