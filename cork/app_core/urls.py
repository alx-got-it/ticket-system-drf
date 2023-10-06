from django.urls import re_path, path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# from app_core.views import TicketViewSet, LocationViewSet, ByLocationViewSet
# from app_core.views import TicketListView, TicketDetailView, TicketByLocationView, TicketCreateView
from app_core.views import TicketViewSet

router = DefaultRouter()
router.register(r'ticket', TicketViewSet, basename='ticket')
# router.register(r'location', LocationViewSet, basename='location')
# router.register(r'tickets_by_location/(?P<location>\w+)/$', ByLocationViewSet, basename='by_location')

urlpatterns = [
    # path('ticket/list/', TicketListView.as_view()),
    # path('ticket/detail/<int:pk>', TicketDetailView.as_view()),
    # path('ticket/create/', TicketCreateView.as_view()),
    # path('ticket/by_location/<str:slug>', TicketByLocationView.as_view()),

    # path('', include(router.urls)),
    # path(r'ticket/by_location/(?P<location>\w+)/$', TicketsByLocationView, name='tickets_by_location'),
]

# app_core_urlpatterns = router.urls

urlpatterns += router.urls
app_core_urlpatterns = urlpatterns
