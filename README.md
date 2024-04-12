# TickItGuru API Documentation

Welcome to the TickItGuru API documentation. TickItGuru provides a platform for purchasing tickets to a variety of events such as concerts, sports events, plays, and more. This document outlines how to use the API effectively.

## Base URL

All API requests should be made to the following base URL:

https://tick-it-api-production.up.railway.app/


## API Endpoints
Below are the various endpoints available, detailed with required parameters and sample requests and responses:

1. List of Venues
Endpoint: /venues

Method: GET

Description:
Retrieve a list of all venues.

Sample Request:

GET /venues

Sample Response:

```json
[
    {
        "id": 4,
        "venue_url": "https://tick-it-api-production.up.railway.app/venues/4",
        "name": "Al HirschField Theatre",
        "city": "New York, NY",
        "address": "302 West 45th Street New York, NY 10036",
        "photo_url": "https://imaging.broadway.com/images/widescreen-169/w358/h201/124943-3.jpg"
    },
    {
        "id": 5,
        "venue_url": "https://tick-it-api-production.up.railway.app/venues/5",
        "name": "Ambassador Theatre",
        "city": "New York, NY",
        "address": "219 West 49th Street New York, NY 10019",
        "photo_url": "https://imaging.broadway.com/images/widescreen-169/w358/h201/124945-3.jpg"
    }
]

2. Venue Details
Endpoint: /venues/<int:pk>

Method: GET

Description:
Fetch detailed information about a specific venue, including upcoming events hosted at the venue.

Sample Request:

GET /venues/4

```json
{
    "id": 4,
    "venue_url": "https://tick-it-api-production.up.railway.app/venues/4",
    "name": "Al HirschField Theatre",
    "city": "New York, NY",
    "address": "302 West 45th Street New York, NY 10036",
    "events": [
        {
            "id": 4,
            "venue": "https://tick-it-api-production.up.railway.app/venues/4",
            "venue_id": 4,
            "name": "Moulin Rouge",
            "date": "July 22, 2023",
            "time": "8:00 PM",
            "type": "Theatre",
            "photo_url": "https://imaging.broadway.com/images/poster-178275/w230/222222/120038-1.jpg",
            "venue_name": "Al HirschField Theatre"
        }
        // More events...
    ],
    "photo_url": "https://imaging.broadway.com/images/widescreen-169/w358/h201/124943-3.jpg"
}

3. List of Events
Endpoint: /events

Method: GET

Description:
Retrieve a list of all events, optionally filterable by type (e.g., "concert", "sport", "theatre").

Sample Request:

GET /events?type=theatre

Sample Response:

```json
[
    {
        "id": 4,
        "venue": "https://tick-it-api-production.up.railway.app/venues/4",
        "venue_id": 4,
        "name": "Moulin Rouge",
        "date": "July 22, 2023",
        "time": "8:00 PM",
        "type": "Theatre",
        "photo_url": "https://imaging.broadway.com/images/poster-178275/w230/222222/120038-1.jpg",
        "venue_name": "Al HirschField Theatre"
    }
    // More events...
]

