from django.contrib import admin
from .models import Event, Attendee, Announcement, ContactMessage, Feedback

admin.site.site_header = "Cloud Event Management Admin"
admin.site.site_title = "Cloud Event Admin Portal"
admin.site.index_title = "Welcome to the Admin Dashboard"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'location', 'capacity')
    search_fields = ('title', 'location')
    list_filter = ('start_time', 'location')
    ordering = ('-start_time',)   


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registered_at')
    search_fields = ('user__username',)
    list_filter = ('event',)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
   list_display = ('name', 'rating', 'created_at')