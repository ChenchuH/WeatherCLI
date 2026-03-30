# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License


from rich import print
from weathercli.helpers.sparklines import sparklines

def compact(weather_info, precp_str):
    print(f"[white]{weather_info["desc_icons"]}  {weather_info["temp"]}{weather_info["temp_unit"]} (feels {weather_info["apparent_temp"]}{weather_info["temp_unit"]}) · {weather_info["desc"]}{precp_str}[/white]")

def detailed(weather_info, precp_str, formated_date_time, wind_dir_cardinal):
    s = sparklines(weather_info["sparklines_range"][:24])
    print(f"[white]{formated_date_time}[/white]") 
    print(f"{s}")
    print(f"[white]{weather_info["desc_icons"]}  {weather_info["temp"]}{weather_info["temp_unit"]} (feels {weather_info["apparent_temp"]}{weather_info["temp_unit"]}) · {weather_info["desc"]}{precp_str}[/white]")
    print(f"[white]Humidity {weather_info["humidity"]}% · Wind {wind_dir_cardinal} {weather_info["wind_speed"]} {weather_info["wind_speed_units"]} · Gusts {weather_info["wind_gust"]} {weather_info["wind_speed_units"]}[/white]")