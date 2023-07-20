from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render
from .models import Venue, Event, Comment
from rest_framework import generics
from .serializers import VenueSerializer, EventSerializer, CommentSerializer


# Create your views here.


class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'city', 'address']


class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['venue', 'name', 'date', 'time', 'type']


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class VenueEventsList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        venue_id = self.kwargs['pk']

        return Event.objects.filter(venue__id=venue_id)


class EventTypeSearch(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        event_type = self.kwargs['event_type']

        return Event.objects.filter(type__iexact=event_type)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'comment', 'event_id']
