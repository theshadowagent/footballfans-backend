from rest_framework import serializers

from sochi_backend.event.models import Event, Club, Match
from sochi_backend.users.models import UserEventUpvote


class EventSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(obj):
        return UserEventUpvote.objects.filter(event_id=obj.id).count()

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('likes', 'author', 'tags')


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        read_only_fields = 'customer'
