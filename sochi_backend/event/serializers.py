from rest_framework import serializers

from sochi_backend.event.models import Event
from sochi_backend.users.models import UserEventUpvote


class EventSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(obj):
        return UserEventUpvote.objects.filter(event_id=obj.id).count()

    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'photo',
                  'likes', 'author', 'match', 'tags')