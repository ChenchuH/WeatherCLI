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

def wind_dir_helper(angle: float) -> str:
    card_points= ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = int((angle + 22.5) % 360 //45)
    return card_points[index]
