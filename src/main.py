from helpers.weather_service import get_weather_data
from helpers.location_service import get_location_data
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print

query = input("> ").strip()

if not query.lower().startswith("weather at "):
    print("Use: Weather at <location>")
    exit()

location = query[11:].strip()


with Progress(SpinnerColumn(), TextColumn("{task.description}"), transient=True) as progress:

    task = progress.add_task("[cyan]Fetching...[/cyan]", total=2)

    lat, long = get_location_data(location)
    progress.update(task, advance=1)

    weather = get_weather_data(lat,long)
    progress.update(task, advance=1)

temp = weather["current"]["temperature_2m"]
unit = weather["current_units"]["temperature_2m"]

print(f"Currently [green]~{temp}{unit}[/green] @ [white]{location}[/white]")