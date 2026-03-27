# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License

from weathercli.helpers.weather_service import get_weather_data
from weathercli.helpers.location_service import get_location_data
from weathercli.helpers.weather_codes import weather_code_values, weather_code_icons, wind_dir_helper

from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print
import requests
from importlib.metadata import version
import argparse 
from datetime import datetime
import sys

CURRENT_VER = version("weathercli")

def chec_ver():
    try:
        res = requests.get("https://api.github.com/repos/ChenchuH/WeatherCLI/releases/latest",timeout=3)
        res.raise_for_status() 
        data = res.json()
        return data["tag_name"].lstrip("v")
    except requests.exceptions.RequestException as e:
        print(f"update check failed {e}")
        return None

def check_for_update():
    latest = chec_ver()
    if latest and latest != CURRENT_VER:
        print(f"[yellow]Update available: {CURRENT_VER} → {latest}[/yellow]")
        print("[cyan]Run: pipx upgrade weathercli[/cyan]")

def parse_args():
    parser = argparse.ArgumentParser(prog="weathercli", description="Get current weather for any location from the terminal.")
    parser.add_argument("location", nargs="*", help="location to search")
    parser.add_argument("--version", action="store_true", help="show version")
    parser.add_argument("--detailed", action="store_true", help="includes humidity, windspeed and direction")
    parser.add_argument("--compact", action="store_true", help="includes only weather and percipitation")
    return parser.parse_args()


def main():

    try:
        args = parse_args()

        if args.version:
            print(CURRENT_VER)
            return
        check_for_update()
        if not args.location:
            print("Use weathercli <location>")
            return
        
        location = " ".join(args.location)
  
        with Progress(SpinnerColumn(), TextColumn("{task.description}"), transient=True) as progress:
            task = progress.add_task("[cyan]Fetching...[/cyan]", total=2)
            lat, long = get_location_data(location)
            progress.update(task, advance=1)
            weather = get_weather_data(lat,long)
            progress.update(task, advance=1)

        code = weather["current"]["weather_code"]
        desc = weather_code_values.get(code, "Unknown")
        desc_icons = weather_code_icons.get(code, "Unknown")

        temp = weather["current"]["temperature_2m"]
        apparent_temp = weather["current"]["apparent_temperature"]
        temp_unit = weather["current_units"]["temperature_2m"]
        wind_speed = weather["current"]["wind_speed_10m"]
        wind_speed_units = weather["current_units"]["wind_speed_10m"]
        wind_gust = weather["current"]["wind_gusts_10m"]
        wind_dir = weather["current"]["wind_direction_10m"]
        humidity = weather["current"]["relative_humidity_2m"]
        date_time = weather["current"]["time"]

        rain = weather["current"]["precipitation"]
        rain_unit = weather["current_units"]["precipitation"]

        snowfall = weather["current"]["snowfall"]
        snowfall_unit = weather["current_units"]["snowfall"]

        wind_dir_cardinal = wind_dir_helper(wind_dir)

        dt = datetime.fromisoformat(date_time)
        formated_date_time = dt.strftime("%m/%d/%Y %I:%M %p")

        precp_str=""

        if snowfall is not None and snowfall > 0:
            precp_str=(f" · Snow {snowfall}{snowfall_unit}")
        elif rain is not None and rain > 0:
            precp_str=(f" · Rain {rain}{rain_unit} ")

        

        if args.compact and args.detailed:
            print("use weathercli --compact OR --detailed not both")
            return
        elif args.compact: 
            print(f"[white]{desc_icons}  {temp}{temp_unit} (feels {apparent_temp}{temp_unit}) · {desc}{precp_str}[/white]")
        elif args.detailed:
            print(f"[white]{formated_date_time}[/white]") 
            print(f"[white]{desc_icons}  {temp}{temp_unit} (feels {apparent_temp}{temp_unit}) · {desc}{precp_str}[/white]")
            print(f"[white]Humidity {humidity}% · Wind {wind_dir_cardinal} {wind_speed} {wind_speed_units} · Gusts {wind_gust} {wind_speed_units}[/white]")
        else:
            print(f"[white]{formated_date_time}[/white]") 
            print(f"[white]{desc_icons}  {temp}{temp_unit} (feels {apparent_temp}{temp_unit}) · {desc}{precp_str}[/white]")
            print(f"[white]Humidity {humidity}% · Wind {wind_dir_cardinal} {wind_speed} {wind_speed_units} · Gusts {wind_gust} {wind_speed_units}[/white]")

    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"error: {e}")




if __name__=="__main__":
    main()