# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License

from weathercli.helpers.weather_service import get_weather_data
from weathercli.helpers.location_service import get_location_data
from weathercli.helpers.weather_codes import wind_dir_helper, weather_dic_lookup
from weathercli.helpers.updater_routine import check_for_update
from weathercli.helpers.output import compact, detailed

from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print
from weathercli.helpers.parse_flags import parse_args
from importlib.metadata import version
from datetime import datetime
import sys

CURRENT_VER = version("weathercli")

def main():
    try:
        args = parse_args()

        if args.version:
            print(CURRENT_VER)
            return
        check_for_update(CURRENT_VER)
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
        
        weather_info = weather_dic_lookup(weather)
        wind_dir_cardinal = wind_dir_helper(weather_info["wind_dir"])
        dt = datetime.fromisoformat(weather_info["date_time"])
        formated_date_time = dt.strftime("%m/%d/%Y %I:%M %p")
        precp_str=""


        if weather_info["snowfall"] is not None and weather_info["snowfall"] > 0:
            precp_str=(f" · Snow {weather_info["snowfall"]}{weather_info["snowfall_unit"]}")
        elif weather_info["rain"] is not None and weather_info["rain"] > 0:
            precp_str=(f" · Rain {weather_info["rain"]}{weather_info["rain_unit"]} ")
        elif args.f:
            if weather_info.get("temp") is not None:
                weather_info["temp"] = round((weather_info["temp"]*9/5)+32,1)
                weather_info["temp_unit"] = "F" 

            if weather_info.get("apparent_temp") is not None:
                weather_info["apparent_temp"] = round((weather_info["apparent_temp"]*9/5)+32,1)
                weather_info["temp_unit"] = "F"

        if args.compact and args.detailed:
            print("use weathercli --compact OR --detailed not both")
            return
        elif args.compact: 
            compact(weather_info, precp_str)
        elif args.detailed:
            detailed(weather_info, precp_str, formated_date_time, wind_dir_cardinal)    
        else:
            detailed(weather_info, precp_str, formated_date_time, wind_dir_cardinal)


    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"error: {e}")

if __name__=="__main__":
    main()