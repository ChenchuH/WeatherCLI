from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="WeatherCLI")

def get_location_data(location_name: str):
    try:
        loc = geolocator.geocode(location_name)
        if loc is None:
            print("Invalid location brocacho, try again twin")
            return None
        else:
            return loc.latitude, loc.longitude
    except Exception as e:
        print(f"error: {e}")
        return None
        
if __name__=="__main__": 
    get_location_data()