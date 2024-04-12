TickItGuru API Documentation
TickItGuru provides a robust platform for purchasing tickets to concerts, sporting events, plays, and other live entertainment options. This API allows you to integrate TickItGuru's services with your applications.

Base URL
All API requests should be directed to the following base URL:

plaintext
Copy code
https://tick-it-api-production.up.railway.app/
Authentication
Access to the API requires an API key. Include your API key in the request header:

markdown
Copy code
Authorization: Bearer YOUR_API_KEY
Replace YOUR_API_KEY with your personal API key.

API Endpoints Overview
Venues
List Venues

GET /venues
Retrieves a list of all venues.
Example Request:
bash
Copy code
curl -X GET https://tick-it-api-production.up.railway.app/venues -H "Authorization: Bearer YOUR_API_KEY"
Venue Details

GET /venues/{id}
Provides detailed information about a specific venue, including related events.
Example Request:
bash
Copy code
curl -X GET https://tick-it-api-production.up.railway.app/venues/4 -H "Authorization: Bearer YOUR_API_KEY"
Events
List Events

GET /events
Retrieves a list of all events, filterable by type, date, or venue.
Example Request:
bash
Copy code
curl -X GET https://tick-it-api-production.up.railway.app/events -H "Authorization: Bearer YOUR_API_KEY"
Event Details

GET /events/{id}
Provides detailed information about a specific event.
Example Request:
bash
Copy code
curl -X GET https://tick-it-api-production.up.railway.app/events/1 -H "Authorization: Bearer YOUR_API_KEY"
Comments
List Comments

GET /comments
Retrieves comments related to events.
Example Request:
bash
Copy code
curl -X GET https://tick-it-api-production.up.railway.app/comments -H "Authorization: Bearer YOUR_API_KEY"
Post Comment

POST /comments
Posts a comment to a specific event.
Example Request:
bash
Copy code
curl -X POST https://tick-it-api-production.up.railway.app/comments -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY" -d '{"name": "John Doe", "comment": "Great event!", "event_id": 1}'
Filters
Search and order functionalities are available on list endpoints to filter results based on specific fields. For example, you can filter events by type or search venues by city.

Error Handling
TickItGuru uses standard HTTP response codes to indicate the success or failure of requests:

200 OK - The request was successful.
400 Bad Request - The request could not be understood by the server.
401 Unauthorized - Authentication failed or user does not have permissions for the action.
404 Not Found - The requested resource was not found.
500 Internal Server Error - A generic error occurred on the server.
Response Example
Here is what a response might look like for a venue listing request:

json
Copy code
{
    "id": 4,
    "venue_url": "https://tick-it-api-production.up.railway.app/venues/4",
    "name": "Al Hirschfield Theatre",
    "city": "New York, NY",
    "address": "302 West 45th Street New York, NY 10036",
    "events": [
        {
            "id": 4,
            "name": "Moulin Rouge",
            "date": "July 22, 2023",
            "time": "8:00 PM",
            "type": "Theatre",
            "photo_url": "https://example.com/path/to/image.jpg",
            "venue_name": "Al Hirschfield Theatre"
        }
    ],
    "photo_url": "https://example.com/path/to/venue/image.jpg"
}
Conclusion
This API documentation should provide all the necessary details to get started with integrating TickItGuru's ticketing services into your application. For further assistance or to request additional features, please contact our support team.
