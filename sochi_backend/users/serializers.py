from django.contrib.auth import get_user_model
from rest_framework import serializers

from sochi_backend.users.models import UserEventUpvote

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserEventUpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserEventUpvote
        fields = '__all__'
        read_only_fields = ['user']
