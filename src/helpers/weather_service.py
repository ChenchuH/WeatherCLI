import requests

def get_weather_data(lat, long):
    res = requests.get("https://api.open-meteo.com/v1/forecast", 
                       params={"latitude":lat, "longitude": long, "current": "temperature_2m"}
                       ).json()
    return res


if __name__=="__main__":
    get_weather_data()