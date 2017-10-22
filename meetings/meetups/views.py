from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Rule
from .serializers import RuleSerializer


class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Rule.objects.filter(user=self.request.user)
