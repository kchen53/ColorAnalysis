# Style Guide
Follow this style guide for Django https://github.com/HackSoftware/Django-Styleguide

## Database
Django includes SQLite database, if we want to use a different database, we will have to set it up in settings.py

## Models
Represents structure of data mapped to a database table

## Views
Logic for processing for processing requests and returning responses

## Business Logic:
### Simple Logic: 
  - Views: Logic relating to handeling request or generating responses
  - Models: logic relating to data validation, data manipulation, interacting with database
### Reusable Logic:
  - Utils module
### Complex Business Logic:
  - Create a Service Layer: seperates business logic into classes/functions dedicated to business rules
### Event-based Logic:
  - Signals: actions triggered by database events
