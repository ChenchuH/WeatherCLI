# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License


from rich import print
from weathercli.helpers.sparklines import sparklines

def compact(weather_info, precp_str):
    print(
        f"[white]{weather_info['desc_icons']}  "
        f"{weather_info['temp']}{weather_info['temp_unit']} · "
        f"feels {weather_info['apparent_temp']}{weather_info['temp_unit']} · "
        f"{weather_info['desc']}{precp_str}[/white]"
    )

def detailed(weather_info, precp_str, formated_date_time, wind_dir_cardinal):
    s = sparklines(weather_info["sparklines_range"][:24])
    print(f"[white]{formated_date_time}[/white]\n")

    print(f"{weather_info['desc_icons']}  {weather_info['desc']}{precp_str}")
    print(f"[white]{weather_info['temp']}{weather_info['temp_unit']}  ·  "
          f"feels {weather_info['apparent_temp']}{weather_info['temp_unit']}[/white]")

    # Sparkline + range
    print(f"[white]24h {s}  {min(weather_info['sparklines_range'][:24]):.1f}{weather_info['temp_unit']}–"f"{max(weather_info['sparklines_range'][:24]):.1f}{weather_info['temp_unit']}[/white]")

    # Secondary stats
    print(f"[white]Humidity {weather_info['humidity']}%  ·  "
          f"Wind {wind_dir_cardinal} {weather_info['wind_speed']} {weather_info['wind_speed_units']}  ·  "
          f"Gusts {weather_info['wind_gust']} {weather_info['wind_speed_units']}[/white]")