from django import forms
from .models import Ride
class info(forms.ModelForm):
    class Meta:
        model=Ride
        fields=[
            'PickupDate',
            'PickupTime',
            'PickupLocation',
            'DropOff',
            'Transfer',
            'ExtraTime',
        ]

