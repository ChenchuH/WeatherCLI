from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="WeatherCLI")

def get_location_data(location_name: str):
    loc = geolocator.geocode(location_name)

    if loc is None:
        print("Invalid location brocacho")
        return None
    
    else:
        return loc.latitude, loc.longitude
        


if __name__=="__main__": 
    get_location_data()