```
wsldev@HomePC-Win11PRO:~$ weathercli
Use weathercli <location>
wsldev@HomePC-Win11PRO:~$ weathercli --h
usage: weathercli [-h] [--version] [--detailed] [--compact] [location ...]

Get current weather for any location from the terminal.

positional arguments:
  location    location to search

options:
  -h, --help  show this help message and exit
  --version   show version
  --detailed  includes humidity, windspeed and direction
  --compact   includes only weather and percipitation
wsldev@HomePC-Win11PRO:~$ weathercli Torrance, CA 90505 --detailed
03/27/2026 11:45 AM
⛅  18.7°C (feels 20.3°C) · Partly cloudy
Humidity 88% · Wind W 8.0 km/h · Gusts 9.4 km/h
wsldev@HomePC-Win11PRO:~$ weathercli Torrance, CA 90505 --compact
⛅  18.7°C (feels 20.3°C) · Partly cloudy
```
