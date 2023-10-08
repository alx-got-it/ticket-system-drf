from django.urls import re_path, path, include
from django.views.decorators.cache import cache_page
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from app_core.views import (TicketListView, TicketDetailView, TicketByLocationView, TicketCreateView,
                            LocationListView, LocationDetailView, UserListView, UserDetailView,
                            UserMeView, TicketMyView)

urlpatterns = [
    path("ticket/list/", cache_page(60 * 60)(TicketListView.as_view()), name="ticket-list"),
    path("ticket/detail/<int:pk>", cache_page(60 * 60)(TicketDetailView.as_view()),
         name="ticket-detail"),
    path("ticket/create/", TicketCreateView.as_view(), name="ticket-create"),
    path("ticket/my/", cache_page(60 * 60)(TicketMyView.as_view()), name="ticket-my"),
    path(
        "ticket/by_location/<slug:slug>",
        cache_page(60 * 60)(TicketByLocationView.as_view()),
        name="ticket-by-location",
    ),
    path("location/list/", cache_page(60 * 60)(LocationListView.as_view()),
         name="location-list"),
    path(
        "location/detail/<slug:slug>",
        cache_page(60 * 60)(LocationDetailView.as_view()),
        name="location-detail",
    ),
    path("user/list/", cache_page(60 * 60)(UserListView.as_view()), name="user-list"),
    path("user/me/", cache_page(60 * 60)(UserMeView.as_view()), name="user-me"),
    path("user/detail/<int:pk>", cache_page(60 * 60)(UserDetailView.as_view()),
         name="user-detail"),
]

app_core_urlpatterns = urlpatterns
