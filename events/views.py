from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.
def events(request):
    
    events_db = Event.objects.filter(is_featured = True)

    data = {
        'events_db': events_db,
    }
    
    return render(request, 'events/events.html', data)


def events_details(request,id):
    single_event = get_object_or_404(Event, pk = id)
    data = {
        'single_event': single_event,
    }
    return render(request, 'events/events_details.html', data)
   