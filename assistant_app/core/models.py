from django.db import models
import uuid


class DemoRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notify_events = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Demo Request"
        verbose_name_plural = "Demo Requests"


class ClientFeedback(models.Model):
    request = models.ForeignKey(DemoRequest, on_delete=models.CASCADE)
    stars = models.IntegerField()

    def __str__(self):
        return f"{self.request.name} - {self.stars}"

    class Meta:
        verbose_name = "Client Feedback"
        verbose_name_plural = "Client Feedback"
