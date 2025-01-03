from rest_framework import serializers
from .models import DemoRequest, ClientFeedback


class DemoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoRequest
        fields = ["id", "name", "email", "phone", "company", "country", "notify_events"]


class ClientFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFeedback
        fields = ["request", "stars"]
