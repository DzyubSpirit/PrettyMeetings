from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Rule, Event, EventUser


class RuleSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Rule
        fields = ('start_time', 'end_time', 'period', 'category', 'user')


class EventSerializer(serializers.ModelSerializer):
    author = UserSerializer

    class Meta:
        model = Event
        fields = ('author', 'place', 'description')


class EventUserSerializer(serializers.ModelSerializer):
    user = UserSerializer
    event = EventSerializer

    class Meta:
        model = EventUser
        fields = ('user', 'event', 'answered', 'accepted')
