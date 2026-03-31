from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('update/<int:event_id>/', views.update_event, name='update_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('my-events/', views.my_events, name='my_events'),
    path('cancel/<int:event_id>/', views.cancel_registration, name='cancel_registration'),
]

