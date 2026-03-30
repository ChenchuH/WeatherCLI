# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License

import requests
from rich import print

def chec_ver():
    try:
        res = requests.get("https://api.github.com/repos/ChenchuH/WeatherCLI/releases/latest",timeout=3)
        res.raise_for_status() 
        data = res.json()
        return data["tag_name"].lstrip("v")
    except requests.exceptions.RequestException as e:
        print(f"update check failed {e}")
        return None

def check_for_update(CURRENT_VER):
    latest = chec_ver()
    if latest and latest != CURRENT_VER:
        print(f"[yellow]Update available: {CURRENT_VER} → {latest}[/yellow]")
        print("[cyan]Run: pipx upgrade weathercli[/cyan]")