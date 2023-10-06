from rest_framework import serializers

from app_core.models import Ticket, Location, Regularity, ToValidate


class TicketSerializer(serializers.ModelSerializer):
    """ Список объявлений """

    location = serializers.SlugRelatedField('name', read_only=True)
    regularity = serializers.SlugRelatedField('name', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ticket
        read_only_fields = ('manager', 'updated')
        exclude = ('validated', 'rejected')
        # depth = 1


class TicketListSerializer(serializers.ModelSerializer):
    """ Список объявлений """

    location = serializers.SlugRelatedField('name', read_only=True)
    regularity = serializers.SlugRelatedField('name', read_only=True)

    class Meta:
        model = Ticket
        read_only_fields = ('manager', 'updated')
        exclude = ('validated', 'rejected')
        # depth = 1


class TicketDetailSerializer(serializers.ModelSerializer):
    """ Объявление """

    location = serializers.SlugRelatedField('name', read_only=True)
    regularity = serializers.SlugRelatedField('name', read_only=True)

    class Meta:
        model = Ticket
        read_only_fields = ('manager', 'updated')
        exclude = ('validated', 'rejected')
        # depth = 1


class TicketByLocationSerializer(serializers.ModelSerializer):
    """ Список объявлений по локации """

    location = serializers.SlugRelatedField('name', read_only=True)
    regularity = serializers.SlugRelatedField('name', read_only=True)

    class Meta:
        model = Ticket
        read_only_fields = ('manager', 'updated')
        exclude = ('validated', 'rejected')


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        read_only_fields = ('name', 'address', 'slug')
        fields = ('name', 'address', 'slug')
        depth = 1
