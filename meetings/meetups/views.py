from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Rule, Event
from .serializers import RuleSerializer, EventSerializer, EventUserSerializer


# todo: remove queryset
class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

