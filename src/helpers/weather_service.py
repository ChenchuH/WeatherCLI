import requests

def get_weather_data(lat, lon):
    try:
        res = requests.get("https://api.open-meteo.com/v1/forecast", 
                        params={"latitude":lat, "longitude": lon, "current": "temperature_2m,weathercode"}, timeout=5)
        #Current means weather values CURRENTLY in the API param
        res.raise_for_status()
        data = res.json()
        return data
    except Exception as e:
        print(f"error: {e}")
        return None

if __name__=="__main__":
    get_weather_data()