from django.contrib import admin
from accounts.models import UserProfile, Room, Reservation

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(Reservation)