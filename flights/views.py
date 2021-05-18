from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def index(request: HttpRequest):
    return render(request, "flights/index.html", {
        'flights': Flight.objects.all()
    })

def flight(request: HttpRequest, flight_id: int):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight).all(),
    })

def book(request: HttpRequest, flight_id: int):
    if request.method == 'POST':
        flight = Flight.objects.get(id=flight_id)
        passenger = Passenger.objects.get(id=int(request.POST['passenger'])) 
        passenger.flights.add(flight)
        return  HttpResponseRedirect(reverse('flight', args=[flight_id]))
    


