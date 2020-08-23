from rest_framework import serializers

from sochi_backend.event.models import Event, Club, Match, Tag
from sochi_backend.users.models import UserEventUpvote
from sochi_backend.users.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = 'customer'


class EventSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()
    # author = UserSerializer()
    tags = serializers.SerializerMethodField()

    @staticmethod
    def get_tags(obj):
        return TagSerializer(obj.tags, many=True).data

    def get_has_liked(self, obj):
        return UserEventUpvote.objects.filter(user=self.context['request'].user,
                                              event_id=obj.id).exists()

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
    home_club = ClubSerializer()
    guest_club = ClubSerializer()

    class Meta:
        model = Match
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        read_only_fields = 'customer'



