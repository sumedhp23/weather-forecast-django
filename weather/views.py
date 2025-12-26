import requests
import os
from django.shortcuts import render
from datetime import datetime, timedelta, timezone

def home(request):
    raw_city = request.GET.get('city', 'Belgaum')
    city = raw_city.title()

    api_key = os.getenv("WEATHER_API_KEY")

    context = {}

    if not api_key:
        context['error'] = "API key not configured"
        return render(request, 'home.html', context)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        context['error'] = data.get('message', 'Something went wrong')
        return render(request, 'home.html', context)

    # 🌍 Timezone handling
    utc_time = datetime.fromtimestamp(data['dt'], tz=timezone.utc)
    city_timezone_offset = timedelta(seconds=data['timezone'])
    city_local_time = utc_time + city_timezone_offset

    # 🇮🇳 Convert to IST
    ist_offset = timedelta(hours=5, minutes=30)
    ist_time = utc_time + ist_offset

    # 🌞 Day or 🌙 Night detection
    hour = city_local_time.hour
    is_day = 6 <= hour < 18

    # 🎨 Background theme logic
    weather_desc = data['weather'][0]['description'].lower()

    if not is_day:
        bg_class = "night"
    elif "rain" in weather_desc:
        bg_class = "rainy"
    elif "cloud" in weather_desc:
        bg_class = "cloudy"
    elif "clear" in weather_desc:
        bg_class = "sunny"
    else:
        bg_class = "default"


    context = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'is_day': is_day,
        'city_time': city_local_time.strftime("%I:%M %p"),
        'ist_time': ist_time.strftime("%I:%M %p"),
        'bg_class': bg_class,
    }

    return render(request, 'home.html', context)
