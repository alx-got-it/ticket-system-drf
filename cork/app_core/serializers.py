from rest_framework import serializers

from app_core.models import Ticket, Location, Regularity, ToValidate


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        read_only_fields = ('manager', 'updated')
        fields = ('header', 'text', 'location', 'regularity', 'contact', 'validated', 'rejected')
