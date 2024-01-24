from django.shortcuts import render, redirect
from .models import CalendarEvent
from .forms import CalendarEventForm, CalendarEventBodyForm
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime
import pytz


def calendar(request):
    user_agent = request.META['HTTP_USER_AGENT']

    all_events = CalendarEvent.objects.all().order_by('-event_start_date')

    # Define the Central Time Zone
    central_timezone = pytz.timezone('America/Chicago')

    # Get the current date in Central Time Zone (as a date object)
    today = datetime.now(central_timezone).date()

    todays_events = []
    upcoming_events = []
    past_events = []

    for event in all_events:
        if event.event_start_date.date() == today:
            todays_events.append(event)
        elif event.event_start_date.date() > today:
            upcoming_events.append(event)
        else:
            past_events.append(event)

    # Concatenate the lists in the desired order
    events = todays_events + upcoming_events + past_events

    context = {
        'events': events,
        'today': today,
    }
    if 'Mobile' in user_agent:
        return render(request, 'event_calendar/calendar.html', context)
    else:
        return render(request, 'event_calendar/calendar.html', context)


def new_event(request):
    user_agent = request.META['HTTP_USER_AGENT']
    event_model = CalendarEvent()
    user = request.user
    forms = CalendarEventForm(request.POST)
    body_form = CalendarEventBodyForm(request.POST)
    dm_body_3 = request.POST.get('foo')
    if request.method == 'POST':
        if forms.is_valid():
            # Assuming both forms need to be saved to a single CalendarEvent instance
            body = dm_body_3
            event_model.body = body
            event_model.title = forms.cleaned_data["title"]
            event_model.color = forms.cleaned_data["color"]
            event_model.event_start_date = forms.cleaned_data["event_start_date"]
            event_model.event_end_date = forms.cleaned_data["event_end_date"]
            event_model.author = user
            event_model.save()
            # Redirect to a new URL after saving the event
            return redirect('calendar')

    else:
        forms = CalendarEventForm()
        body_form = CalendarEventBodyForm()

    context = {
        'event_forms': forms,
        'bodyform': body_form,
    }
    if 'Mobile' in user_agent:
        return render(request, 'event_calendar/new_event.html', context=context)
    else:
        return render(request, 'event_calendar/new_event.html', context=context)