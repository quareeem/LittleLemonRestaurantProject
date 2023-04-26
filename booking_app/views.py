import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.core.exceptions import ValidationError
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt

from .forms import MenuForm, BookingForm
from .models import Menu, Booking



def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    context = {'form': form}
    return render(request, 'book.html', context)

def reservations(request):
    return render(request, 'bookings.html')

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        print('entering post request (bookings view)...')
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
            return JsonResponse({'status': 'ok', 'message': 'Reservation successful'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Reservation already exists'})
    
    date = request.GET.get('date', None)
    # if date == '':
    #     raise ValidationError("Invalid date format. Must be in YYYY-MM-DD format.")
    if not date:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serialize('json', bookings)
    data = json.loads(booking_json)
    data = {idx: v for idx, v in enumerate(json.loads(booking_json))}
    return JsonResponse(data, content_type='application/json')



def menu(request):
    menu = Menu.objects.all()
    context = {'menu': menu}
    return render(request, 'menu.html', {'menu': context})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    context = {'menu_item': menu_item}
    return render(request, 'menu_item.html', context) 