from django.urls import path

from sochi_backend.event.views import EventDetailView, EventsListView, MatchRetrieveView, NextMatchView, MatchesListView

app_name = "event"

urlpatterns = [
    path("events", EventsListView.as_view()),
    path("events/<int:pk>", EventDetailView.as_view(), name='event-detail'),
    path("matches/next", NextMatchView.as_view()),
    path("matches/<int:pk>", MatchRetrieveView.as_view()),
    path("matches", MatchesListView.as_view(), name='match-detail'),
]
