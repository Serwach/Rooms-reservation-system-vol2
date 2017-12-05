from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# -*- coding: utf-8 -*-

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
         user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Room(models.Model):
    number = models.CharField(max_length=100)
    building = models.CharField(max_length=100)

    def __str__(self):
        return self.number + ' ' + self.building

class Reservation(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    roomid = models.ForeignKey(Room, on_delete=models.CASCADE)
    time1 = models.DateTimeField()
    time2 = models.DateTimeField()

    def __str__(self):
        return format(str(self.time1) + ' ' + str(self.time2))