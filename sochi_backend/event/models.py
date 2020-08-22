from django.db import models
from django.utils import timezone
from django.contrib import admin


class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    photo = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE,
                               blank=True, null=True)
    match = models.ForeignKey('Match', on_delete=models.CASCADE,
                              blank=True, null=True)
    is_home_event = models.BooleanField(default=True)
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
    city = models.CharField(max_length=128, blank=True, null=True)


class Tournament(models.Model):
    TYPE_LEAGUE = "league"
    TYPE_CUP = "cup"

    name = models.CharField(max_length=128)
    logo_url = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20, default=TYPE_LEAGUE)


class Match(models.Model):
    home_club = models.ForeignKey('Club', on_delete=models.CASCADE,
                                  related_name='club_home_matches',
                                  blank=True, null=True)
    guest_club = models.ForeignKey('Club', on_delete=models.CASCADE,
                                   related_name='club_guest_matches',
                                   blank=True, null=True)
    season = models.ForeignKey('Season', on_delete=models.CASCADE,
                               blank=True, null=True)
    stadium = models.CharField(max_length=256, blank=True, null=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE,
                                   blank=True, null=True)
    date_time = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ['-date_time']


class Season(models.Model):
    slug = models.CharField(max_length=10)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ["-order"]


class Ticket(models.Model):
    match = models.ForeignKey('Match', on_delete=models.CASCADE,
                              blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                 blank=True, null=True)
    date_bought = models.DateTimeField(default=timezone.now, blank=True)


class FanPass(models.Model):
    pass_id = models.CharField(max_length=128, blank=True, null=True)
    customer = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                 blank=True, null=True)
    date_bought = models.DateTimeField(default=timezone.now, blank=True)


admin.site.register(Event)
admin.site.register(FanPass)
admin.site.register(Match)
admin.site.register(Club)
admin.site.register(Tournament)
admin.site.register(Ticket)
admin.site.register(Season)
admin.site.register(Tag)
