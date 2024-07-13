from django.db import models

class BusInfo(models.Model):
    busNo = models.TextField(max_length=255)
    driverName = models.TextField()
    driverContact = models.PositiveBigIntegerField()
    busRoute = models.TextField()


class Studentinfo(models.Model):
    collegeid = models.IntegerField(db_column='collegeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60, blank=True, null=True)
    branch = models.CharField(max_length=50, blank=True, null=True)
    collegename = models.CharField(db_column='collegeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    busno = models.CharField(max_length=20, db_column='busNo', blank=True, null=True)  # Field name made lowercase.
    contact = models.IntegerField(blank=True, null=True)
    emailid = models.CharField(db_column='emailID', max_length=60, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=30, blank=True, null=True)
    boardingpt = models.CharField(db_column='boardingPt', max_length=40, blank=True, null=True)  # Field name made lowercase.


