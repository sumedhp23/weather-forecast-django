import requests
import os
from django.shortcuts import render
from datetime import datetime, timedelta, timezone

def home(request):
    raw_city = request.GET.get("city", "Belgaum")
    city = raw_city.title()

    api_key = os.getenv("WEATHER_API_KEY")
    context = {}

    if not api_key:
        context["error"] = "API key not configured"
        return render(request, "home.html", context)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        context["error"] = data.get("message", "Something went wrong")
        return render(request, "home.html", context)

    # ✅ CORRECT TIME HANDLING (PRODUCTION GRADE)
    now_utc = datetime.now(timezone.utc)

    city_offset = timedelta(seconds=data["timezone"])
    city_local_time = now_utc + city_offset

    ist_offset = timedelta(hours=5, minutes=30)
    ist_time = now_utc + ist_offset

    # 🌞 Day / 🌙 Night
    hour = city_local_time.hour
    is_day = 6 <= hour < 18

    # 🎨 Background logic
    weather_desc = data["weather"][0]["description"].lower()

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
        "city": city,
        "temperature": round(data["main"]["temp"]),
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "is_day": is_day,
        "city_time": city_local_time.strftime("%I:%M %p"),
        "ist_time": ist_time.strftime("%I:%M %p"),
        "bg_class": bg_class,
    }

    return render(request, "home.html", context)