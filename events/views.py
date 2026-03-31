from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
from .models import Event, Attendee, Announcement, ContactMessage, Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time', 'location', 'capacity']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'rating', 'comment']

# User Login
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'events/signup.html', {'form': form})
    
# Home page
def home(request):
    search_query = request.GET.get('search', '')
    message = request.GET.get('message', '')

    if search_query:
        events = Event.objects.filter(title__icontains=search_query)
    else:
        events = Event.objects.all()

    announcements = Announcement.objects.all().order_by('-created_at')

    for event in events:
        event.registered_count = event.attendees.count()
        event.remaining_spots = event.capacity - event.registered_count

    trending_events = sorted(events, key=lambda x: x.registered_count, reverse=True)[:3]

    total_events = Event.objects.count()
    total_attendees = Attendee.objects.count()

    return render(request, 'events/home.html', {
        'events': events,
        'announcements': announcements,
        'trending_events': trending_events,
        'search_query': search_query,
        'total_events': total_events,
        'total_attendees': total_attendees,
        'message': message,
    })


# Update Event
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm(instance=event)

    return render(request, 'events/update.html', {'form': form})


# Delete Event
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('home')


@login_required
def my_events(request):
    my_registrations = Attendee.objects.filter(user=request.user)

    return render(request, 'events/my_events.html', {
        'my_registrations': my_registrations
    })


# Register Event
@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    already_registered = Attendee.objects.filter(user=request.user, event=event).exists()

    if already_registered:
        return redirect('/?message=already_registered')
    elif event.attendees.count() >= event.capacity:
        return redirect('/?message=event_full')
    else:
        Attendee.objects.create(user=request.user, event=event)
        return redirect('/?message=success')


# Cancel Event
@login_required
def cancel_registration(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    Attendee.objects.filter(
        user=request.user,
        event=event
    ).delete()

    return redirect('my_events')


# Contact Message
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'events/contact.html', {
                'form': ContactForm(),
                'success': "Message sent successfully!"
            })
    else:
        form = ContactForm()

    return render(request, 'events/contact.html', {'form': form})


# Feedback
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'events/feedback.html', {
                'form': FeedbackForm(),
                'success': "Feedback submitted successfully!"
            })
    else:
        form = FeedbackForm()

    return render(request, 'events/feedback.html', {'form': form})