from django.urls import path
from . import views


urlpatterns = [
    path('', views.VenueList.as_view(), name='venue_list'),
    path('events', views.EventList.as_view(), name='event_list'),
    path('venues/<int:pk>', views.VenueDetail.as_view(), name='venue_detail'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
    path('venues', views.VenueList.as_view(), name='venue_list'),
    path('venues/<int:pk>/events/', views.VenueEventsList.as_view(), name='venue-events-list'),
    path('events/search/type/<str:event_type>/', views.EventTypeSearch.as_view(), name='event-type-search')
]