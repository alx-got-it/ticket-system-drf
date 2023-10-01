from django.urls import re_path
from rest_framework.routers import DefaultRouter

from app_core.views import TicketViewSet

router = DefaultRouter()
router.register(r"ticket", TicketViewSet, basename="ticket")
app_core_urlpatterns = router.urls
