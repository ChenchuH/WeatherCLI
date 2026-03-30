# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License
import requests

def get_weather_data():
    res = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude":"33.8369", "longitude":"-118.3407", "hourly": "temperature_2m"}, timeout=5)
    #Torrance Cords for testing
    data = res.json()
    return data


def sparklines(temp_range_day):
    sparklines_graph = "▁▂▃▄▅▆▇█"
    mn, mx = min(temp_range_day), max(temp_range_day)

    if mx - mn == 0:
        return sparklines_graph[0]*len(temp_range_day)
    
    return "".join(sparklines_graph[int((x - mn) / (mx - mn) * (len(sparklines_graph) - 1))] for x in temp_range_day)

data = get_weather_data()

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"][:24]

#temporary data
print("the next 24 hours")
s=sparklines(temps)
print(s)



