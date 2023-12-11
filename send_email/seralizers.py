from rest_framework import serializers
from .models import SendMessage

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMessage
        fields = '__all__'