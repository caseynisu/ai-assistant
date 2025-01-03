from rest_framework import viewsets
from .models import DemoRequest, ClientFeedback
from .serializers import DemoRequestSerializer, ClientFeedbackSerializer
from django.shortcuts import render


class DemoRequestViewSet(viewsets.ModelViewSet):
    queryset = DemoRequest.objects.all()
    serializer_class = DemoRequestSerializer

    def retrieve(self, request, *args, **kwargs):
        template_name = "ai-assistant.html"
        instance = self.get_object()
        context = {"instance": instance}
        return render(request, template_name, context)


class ClientFeedbackViewSet(viewsets.ModelViewSet):
    queryset = ClientFeedback.objects.all()
    serializer_class = ClientFeedbackSerializer
