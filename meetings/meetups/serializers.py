from rest_framework import serializers

from .models import Rule

from users.serializers import UserSerializer



class RuleSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Rule
        fields = ('start_time', 'end_time', 'period', 'category', 'user')
