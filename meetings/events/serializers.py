from rest_framework import serializers

from .models import Event

from users.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    owner = UserSerializer

    class Meta:
        model = Event
        fields = ('start_time', 'end_time', 'title', 'description', 'owner')
