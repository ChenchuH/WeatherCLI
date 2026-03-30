# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License

weather_code_values = {
0: "Clear sky", 
1: "Mainly clear", 
2: "Partly cloudy", 
3: "Overcast", 
45: "Fog", 
48: "Depositing rime fog", 
51: "Light drizzle", 
53: "Moderate drizzle", 
55: "Dense drizzle", 
61: "Slight rain", 
63: "Moderate rain", 
65: "Heavy rain", 
71: "Slight snow", 
73: "Moderate snow", 
75: "Heavy snow", 
80: "Rain showers", 
95: "Thunderstorm", 
}

weather_code_icons = {
0: ":sun:",
1: ":sun_behind_small_cloud:",
2: ":sun_behind_cloud:",
3: ":cloud:",
45: ":fog:",
48: ":fog:",
51: ":cloud_with_rain:",
53: ":cloud_with_rain:",
55: ":cloud_with_rain:",
61: ":cloud_with_rain:",
63: ":cloud_with_rain:",
65: ":cloud_with_rain:",
71: ":snowflake:",
73: ":snowflake:",
75: ":snowflake:",
80: ":cloud_with_rain:",
95: ":cloud_with_lightning:",
}

def wind_dir_helper(angle: float) -> str:
    card_points= ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = int((angle + 22.5) % 360 //45)
    return card_points[index]

def weather_dic_lookup(weather):
    code = weather["current"]["weather_code"]
    
    return {
        "code": code,
        "desc": weather_code_values.get(code, "Unknown"),
        "desc_icons": weather_code_icons.get(code, "Unknown"),
        "sparklines_range": weather["hourly"]["temperature_2m"],
        "temp": weather["current"]["temperature_2m"],
        "apparent_temp": weather["current"]["apparent_temperature"],
        "temp_unit": weather["current_units"]["temperature_2m"],
        "wind_speed": weather["current"]["wind_speed_10m"],
        "wind_speed_units": weather["current_units"]["wind_speed_10m"],
        "wind_gust": weather["current"]["wind_gusts_10m"],
        "wind_dir": weather["current"]["wind_direction_10m"],
        "humidity": weather["current"]["relative_humidity_2m"],
        "date_time": weather["current"]["time"],
        "rain": weather["current"]["precipitation"],
        "rain_unit": weather["current_units"]["precipitation"],
        "snowfall": weather["current"]["snowfall"],
        "snowfall_unit": weather["current_units"]["snowfall"],
    }