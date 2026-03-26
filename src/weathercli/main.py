from weathercli.helpers.weather_service import get_weather_data
from weathercli.helpers.location_service import get_location_data
from weathercli.helpers.weather_codes import weather_code_values
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print
import requests
import importlib.metadata

CURRENT_VER = importlib.metadata.version("weathercli")

def chec_ver():
    try:
        res = requests.get("https://api.github.com/repos/ChenchuH/WeatherCLI/releases/latest",timeout=3)
        data = res.json()
        return data["tag_name"].lstrip("v")
    except:
        None

def check_for_update():
    latest = chec_ver()
    if latest and latest != CURRENT_VER:
        print(f"[yellow]Update available: {CURRENT_VER} → {latest}[/yellow]")
        print("[cyan]Run: pipx upgrade weathercli[/cyan]")

def main():
    check_for_update()
    query = input("> ").strip()
    if not query.lower().startswith("weather at "):
        print("Use: Weather at <location>")
        exit()
    location = query[11:].strip()

    try:
        with Progress(SpinnerColumn(), TextColumn("{task.description}"), transient=True) as progress:
            task = progress.add_task("[cyan]Fetching...[/cyan]", total=2)
            lat, long = get_location_data(location)
            progress.update(task, advance=1)
            weather = get_weather_data(lat,long)
            progress.update(task, advance=1)

        code = weather["current"]["weathercode"]
        desc = weather_code_values.get(code, "Unknown")

        temp = weather["current"]["temperature_2m"]
        unit = weather["current_units"]["temperature_2m"]

        print(f"Currently [bold][white]~{temp}{unit} - {desc}[/white][/bold]")

    except Exception as e:
        print(f"error: {e}")

if __name__=="__main__":
    main()