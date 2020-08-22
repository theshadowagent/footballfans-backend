from rest_framework import generics
from rest_framework.permissions import AllowAny

from sochi_backend.event.models import Event
from sochi_backend.event.serializers import EventSerializer


class ListEventsView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        match_id = self.request.query_params.get('match_id', None)
        if not match_id:
            return Event.objects.all()
        return Event.objects.filter(match_id=match_id)

