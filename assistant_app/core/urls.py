from rest_framework.routers import DefaultRouter
from .views import DemoRequestViewSet, ClientFeedbackViewSet

router = DefaultRouter()
router.register(r"demo-requests", DemoRequestViewSet, basename="demo-request")
router.register(r"client-feedback", ClientFeedbackViewSet, basename="client-feedback")

urlpatterns = router.urls
