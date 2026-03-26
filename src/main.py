from helpers.weather_service import get_weather_data
from helpers.location_service import get_location_data
from helpers.weather_codes import weather_code_values
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print

def main():
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