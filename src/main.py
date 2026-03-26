from helpers.weather_service import get_weather_data
from helpers.location_service import get_location_data
from rich.progress import Progress, SpinnerColumn, TextColumn

query = input("> ").strip()

if not query.lower().startswith("weather at "):
    print("Use: Weather at <location>")
    exit()

location = query[11:].strip()


with Progress(SpinnerColumn(), TextColumn("[cyan]Fetching...")) as progress:

    task = progress.add_task("work", total=2)

    lat, long = get_location_data(location)
    progress.update(task, advance=1)

    weather = get_weather_data(lat,long)
    progress.update(task, advance=1)

temp = weather["current"]["temperature_2m"]
unit = weather["current_units"]["temperature_2m"]

print(f"Currently ~{temp}{unit} @ {location}")