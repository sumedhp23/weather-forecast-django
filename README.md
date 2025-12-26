# Weather Forecast Web Application

This project is a Django-based weather forecasting web application built completely from scratch.  
It allows users to search for any city and view real-time weather information along with accurate local time and Indian Standard Time (IST).

The application focuses not just on functionality, but also on user experience — dynamically adapting its visuals based on the weather conditions and time of day at the searched location.

---

## What This Application Does

- Fetches real-time weather data using the OpenWeather API  
- Displays temperature, humidity, and weather description for any city  
- Calculates the **local time of the searched city** using timezone offsets  
- Displays the **current IST time** for reference  
- Automatically detects **day or night** at the location  
- Updates background themes and icons based on weather and time  
- Handles invalid inputs and API failures gracefully  

---

## Key Features

- Supports weather lookup for **200,000+ cities worldwide**
- Timezone-aware logic for accurate local time calculation
- Dynamic UI themes for sunny, cloudy, rainy, and night conditions
- Animated, condition-based weather icons
- Secure API key management using environment variables
- Clean and minimal card-based interface
- User-friendly error handling with no runtime crashes

---

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **API:** OpenWeather REST API
- **Environment Management:** python-dotenv
- **Version Control:** Git & GitHub
- **Development Environment:** macOS, VS Code

---

## Project Structure

weather-forecast-django/
│
├── weather_project/
│ ├── weather/
│ │ ├── views.py
│ │ ├── urls.py
│ │ └── templates/
│ │ └── home.html
│ ├── settings.py
│ ├── urls.py
│ └── manage.py
│
├── .gitignore
├── requirements.txt
└── README.md

---

## Useful Link

https://openweathermap.org/api

---

## Author

Sumedh Patil
