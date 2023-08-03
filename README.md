# Weather-App

Weather App is a Python application that utilizes various libraries to retrieve geographic and time-related information based on user input. It leverages the tkinter library for the graphical user interface (GUI) and integrates functionality from geopy, timezonefinder, datetime, requests, pytz, and PIL libraries to provide users with location-based data.

Features:

* Geographic Location: The app allows users to input a location city, and it uses the geopy library along with the Nominatim geocoding service to retrieve the latitude and longitude coordinates of the specified location.
* Timezone Information: Once the geographic coordinates are obtained, the app utilizes the timezonefinder library to determine the timezone of the provided location.
* Current Time: The app displays the current time of the specified location using the datetime library and the determined timezone.
* Weather Information: Additionally, the app fetches weather data for the given location using the requests library to make API calls to a weather service: OpenWeatherMap.
* Display Image: The app also showcases images relevant to the specified location weather using the PIL library to load and display images.
