from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE,
                               blank=True, null=True)
    match = models.ForeignKey('Match', on_delete=models.CASCADE,
                              blank=True, null=True)
    tags = models.ForeignKey('Tag',
                             on_delete=models.CASCADE,
                             blank=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    type = models.IntegerField(default=0)

    TYPE_NEUTRAL = 0
    TYPE_GOOD = 1
    TYPE_BAD = 2


class Club(models.Model):
    name = models.CharField(max_length=128)
    logo_url = models.CharField(max_length=255, blank=True, null=True)


class Match(models.Model):
    home_club = models.ForeignKey('Club', on_delete=models.CASCADE,
                                  related_name='club_home_matches',
                                  blank=True, null=True)
    guest_club = models.ForeignKey('Club', on_delete=models.CASCADE,
                                   related_name='club_guest_matches',
                                   blank=True, null=True)
    date_time = models.DateTimeField(default=timezone.now, blank=True)


class Ticket(models.Model):
    match = models.ForeignKey('Match', on_delete=models.CASCADE,
                              blank=True, null=True)
    customer = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                 blank=True, null=True)
    date_bought = models.DateTimeField(default=timezone.now, blank=True)


class FanPass(models.Model):
    pass_id = models.CharField(max_length=128, blank=True, null=True)
    customer = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                 blank=True, null=True)
    date_bought = models.DateTimeField(default=timezone.now, blank=True)
