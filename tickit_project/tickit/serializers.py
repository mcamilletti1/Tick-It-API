from rest_framework import serializers
from .models import *


class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )

    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )

    class Meta:
        model = Event
        fields = ('id', 'venue', 'venue_id', 'name',
                  'date', 'time', 'type', 'photo_url')


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        many=True,
        read_only=True
    )

    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue_detail'
    )

    class Meta:
        model = Venue
        fields = ('id', 'venue_url', 'name', 'city',
                  'address', 'events', 'photo_url')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        read_only=True
    )

    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event'
    )

    class Meta:
        model = Comment
        fields = ('name', 'comment', 'event_id')
