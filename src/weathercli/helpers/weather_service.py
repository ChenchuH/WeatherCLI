# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License

import requests

def get_weather_data(lat, lon):
    try:
        res = requests.get("https://api.open-meteo.com/v1/forecast", 
                        params={"latitude":lat, "longitude":lon, "current": "temperature_2m,apparent_temperature,wind_speed_10m,wind_direction_10m,wind_gusts_10m,relative_humidity_2m,weather_code,precipitation,snowfall", 
                                "hourly": "temperature_2m",
                                "timezone": "auto"}, 
                                timeout=5)
   
   
        res.raise_for_status()
        data = res.json()
        return data
    except Exception as e:
        print(f"error: {e}")
        return None

if __name__=="__main__":
    get_weather_data()