from django.contrib import admin
from busroutings.models import BusInfo
from busroutings.models import Studentinfo

class BusInfos(admin.ModelAdmin):
    data = ('busNo', 'driverName', 'driverContact', 'busRoute')

class StudentInfos(admin.ModelAdmin):
    data = ('collegeid', 'name', 'branch', 'collegename', 'year', 'busno', 'contact', 'emailid', 'password', 'boardingpt')

admin.site.register(BusInfo, BusInfos)
admin.site.register(Studentinfo, StudentInfos)
