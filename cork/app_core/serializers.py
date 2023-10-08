from django.contrib.auth.models import User
from rest_framework import serializers

from app_core.models import Ticket, Location, Regularity, ToValidate


class TicketSerializer(serializers.ModelSerializer):
    location = serializers.ReadOnlyField(source="location.name")
    regularity = serializers.ReadOnlyField(source="regularity.name")
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Ticket
        read_only_fields = ("updated", "owner")
        exclude = ("validated", "rejected")
        depth = 1


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketByLocationSerializer(TicketSerializer):
    location_id = serializers.ReadOnlyField(source="location.id")


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "email", "tickets"]
        depth = 1
