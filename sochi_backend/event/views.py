from django.db.models.aggregates import Count
from rest_framework import generics, views
from rest_framework.permissions import AllowAny

from sochi_backend.event.models import Event, Match
from sochi_backend.event.serializers import EventSerializer, MatchSerializer


class EventsListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        match_id = self.request.query_params.get('match_id', None)
        if match_id:
            return (
                Event.objects
                .filter(match_id=match_id)
                .annotate(likes_count=Count('usereventupvote__id', distinct=True))
                .order_by("-likes_count")
            )
        return (
                Event.objects
                .annotate(likes_count=Count('usereventupvote__id', distinct=True))
                .order_by("-likes_count")
            )


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)


class MatchesListView(generics.ListAPIView):
    serializer_class = MatchSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        tournament_id = self.request.query_params.get('tournament_id', None)
        season_id = self.request.query_params.get('season_id', None)
        if season_id:
            return Match.objects.filter(season_id=season_id)
        if tournament_id:
            return Match.objects.filter(tournament_id=tournament_id)
        return Match.objects.all()


class NextMatchView(generics.ListAPIView):
    serializer_class = MatchSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        matches = Match.objects.order_by('-date_time')
        if matches:
            return matches[:1]
        return None


class MatchRetrieveView(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = (AllowAny,)

