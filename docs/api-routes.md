# API Routes

## Events

POST `/api/events` - Create a new event  
GET `/api/events` - Fetch all event  
GET `/api/events/:event_id` - Fetch a specific event  
PATCH `/api/events/:event_id` - Update an existing event  
DELETE `/api/events/:event_id` - Delete a event  

GET `/api/events/:event_id/tickets` - Fetch tickets of a specific event  
POST `/api/events/:event_id/purchase` - Purchase a certain number of tickets  

## Customers

POST `/api/customers` - Create a new customer  
GET `/api/customers` - Fetch all customer  
GET `/api/customers/:customer_id` - Fetch a specific customer  
PATCH `/api/customers/:customer_id` - Update an existing customer  
DELETE `/api/customers/:customer_id` - Delete a customer  

GET `/api/customers/:customer_id/budget` - Fetch budget of a specific customer  
GET `/api/customers/:customer_id/tickets?order_date=&event_date=` - Fetch tickets of a specific customer  
