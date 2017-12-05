from django.contrib import admin
from system.models import UserProfile, Room, Reservation

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(Reservation)