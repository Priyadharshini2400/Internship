from django.shortcuts import render
from .models import Ride
from .forms import info

# Create your views here.
    
def home(request):
    if request.method == 'POST':
        ride = Ride(
            PickupDate=request.POST.get("PickupDate"),
            PickupTime=request.POST.get("PickupTime"),
            PickupLocation=request.POST.get("PickupLocation"),
            DropOff=request.POST.get("DropOff"),
            
        )
        ride.save()
        return render(request, 'home.html', {'success': True})
    
    return render(request, 'home.html')
   



def rates(request):
    if request.method == 'POST':
        ride = Ride(
            PickupDate=request.POST.get("PickupDate"),
            PickupTime=request.POST.get("PickupTime"),
            PickupLocation=request.POST.get("PickupLocation"),
            DropOff=request.POST.get("DropOff"),
            Transfer=request.POST.get("Transfer"),
            ExtraTime=request.POST.get("ExtraTime"),
        )
        ride.save()
        return render(request, 'rates.html', {'success': True})
    
    return render(request, 'rates.html')

def niagara(request):
     if request.method == 'POST':
        ride = Ride(
            PickupDate=request.POST.get("PickupDate"),
            PickupTime=request.POST.get("PickupTime"),
            PickupLocation=request.POST.get("PickupLocation"),
            DropOff=request.POST.get("DropOff"),
            Transfer=request.POST.get("Transfer"),
            ExtraTime=request.POST.get("ExtraTime"),
        )
        ride.save()
        return render(request, 'niagara.html', {'success': True})
    
     return render(request, 'niagara.html')
    
def ajax(request):
    if request.method == 'POST':
        ride = Ride(
            PickupDate=request.POST.get("PickupDate"),
            PickupTime=request.POST.get("PickupTime"),
            PickupLocation=request.POST.get("PickupLocation"),
            DropOff=request.POST.get("DropOff"),
            Transfer=request.POST.get("Transfer"),
            ExtraTime=request.POST.get("ExtraTime"),
        )
        ride.save()
        return render(request, 'ajax.html', {'success': True})
    
    return render(request, 'ajax.html')


def ancaster(request):
    return render(request,'Ancaster.html')

def blog(request):
    if request.method == 'POST':
        ride = Ride(
            PickupDate=request.POST.get("PickupDate"),
            PickupTime=request.POST.get("PickupTime"),
            PickupLocation=request.POST.get("PickupLocation"),
            DropOff=request.POST.get("DropOff"),
            Transfer=request.POST.get("Transfer"),
        )
        ride.save()
        return render(request, 'blog.html', {'success': True})
    
    return render(request, 'blog.html')
   