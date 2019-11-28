from django.db import models


class checkin(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    no=models.CharField(max_length=100)
    hostname=models.CharField(max_length=100)
    hostemail=models.CharField(max_length=100)
    hostno=models.CharField(max_length=100)
    isCheckOut = models.BooleanField()
    checkInTime = models.CharField(max_length=20)
    checkOutTime = models.CharField(max_length=20)
