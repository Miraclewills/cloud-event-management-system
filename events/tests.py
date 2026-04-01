from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event, Attendee, Announcement
from datetime import datetime
import pytz

class EventViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            start_time=datetime(2026, 6, 1, 9, 0, tzinfo=pytz.UTC),
            end_time=datetime(2026, 6, 1, 17, 0, tzinfo=pytz.UTC),
            location='Test Location',
            capacity=100
        )

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_feedback_page(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_login_required_for_my_events(self):
        response = self.client.get(reverse('my_events'))
        self.assertEqual(response.status_code, 302)

    def test_register_event_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('register_event', args=[self.event.id])
        )
        self.assertEqual(response.status_code, 302)
