from rest_framework import serializers
from .models import information, information


class informationSerializer(serializers.ModelSerializer):
    class Meta:
        model = information
        fields = ['slackUsername', 'backend', 'age', 'bio']