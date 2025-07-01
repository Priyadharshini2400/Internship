from django.db import models

# Create your models here.
class Ride(models.Model):

    PickupDate=models.DateField()
    PickupTime=models.TimeField()
    PickupLocation=models.CharField(max_length=200)
    DropOff=models.CharField(max_length=200)
    Transfer=models.CharField()
    ExtraTime=models.CharField()