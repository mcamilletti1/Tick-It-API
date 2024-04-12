TickItGuru API Documentation
Welcome to the official API documentation for TickItGuru, your premier service for discovering and purchasing tickets for a wide array of events including concerts, sports events, theater productions, and more. Below you will find detailed instructions on how to effectively utilize the API to enhance your application or service with live event ticketing functionality.

API Base URL
All API requests should be made to the following base URL:

arduino
Copy code
https://tick-it-api-production.up.railway.app/
This base URL serves as the entry point for all API endpoints described below.

Authentication
Some endpoints require authentication. Ensure to include your API key in the header of such requests:

css
Copy code
Authorization: Bearer {YOUR_API_KEY}
Replace {YOUR_API_KEY} with your actual API key provided upon your API account setup.

API Endpoints
Below are the various endpoints available, detailed with required parameters and sample requests and responses:

Venues
List All Venues
Endpoint: GET /venues
Description: Retrieve a list of all venues.
Sample Request:
bash
Copy code
curl -X GET https://tick-it-api-production.up.railway.app/venues
Sample Response:
json
Copy code
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
Get Venue Details
Endpoint: GET /venues/{venue_id}
Description: Fetch detailed information about a specific venue, including upcoming events hosted at the venue.
Sample Request:
bash
Copy code
curl -X GET https://tick-it-api-production.up.railway.app/venues/4
Sample Response:
json
Copy code
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
Events
List All Events
Endpoint: GET /events
Description: Retrieve a list of all events, optionally filterable by type (e.g., "concert", "sport", "theatre").
Parameters:
type: Filter events by type. Example: type=theatre
Sample Request:
bash
Copy code
curl -X GET https://tick-it-api-production.up.railway.app/events?type=theatre
Sample Response:
json
Copy code
[
    {
        "id": 4,
        "venue": "https://tick-it-api-production.up.railway.app/venues/4",
        "venue_id": 4,
        "name": "Moulin Rouge",
        "date": "July 22, 2023",
        "time": "8:00 PM",
        "type": "Theatre",
        "photo_url": "https://imaging.broadway.com/images/poster-178275/w230/222222
