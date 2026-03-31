## 🌤️ WEATHER CLI
Fast • Simple • Terminal Weather

A fast, minimal command-line weather tool powered by Open-Meteo.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
---

## Sample commands
```
wsldev@HomePC-Win11PRO:~$ weathercli
Use weathercli <location>

wsldev@HomePC-Win11PRO:~/projects/WeatherCLI$ weathercli -h
usage: weathercli [-h] [--version] [--detailed] [--compact] [--f] [location ...]

Get current weather for any location from the terminal.

positional arguments:
  location    location to search

options:
  -h, --help  show this help message and exit
  --version   show version
  --detailed  includes humidity, windspeed and direction
  --compact   includes only weather and percipitation
  --f         Display units in Fahrenheit as opposed to default Celcius, ex. weathercli <location> --f or weathercli <location> <detailed/compact flag> --f

wsldev@HomePC-Win11PRO:~$ weathercli Torrance, CA 90505 --detailed
03/30/2026 12:45 PM
▁▂▁▁▁▁▁▁▂▂▄▄▅▆▆▇█▇▆▄▄▄▃▃
☁  19.3°C (feels 19.6°C) · Overcast
Humidity 81% · Wind SE 11.6 km/h · Gusts 14.8 km/h

wsldev@HomePC-Win11PRO:~$ weathercli Torrance, CA 90505 --compact
☁  19.3°C (feels 19.6°C) · Overcast
```
## Installation

### Recommended (via pipx)

```bash
pipx install "git+https://github.com/ChenchuH/WeatherCLI.git"
```

> Requires `pipx`

---

### Install pipx (Ubuntu / WSL)

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Verify installation:

```bash
pipx --version
```

---

## Usage

```bash
weathercli <location>
```
default is the ```--detailed``` output, to get the compact output you must prompt the flag ```--compact```

### Examples

```bash
weathercli "Los Angeles, CA" 
weathercli "New York"
weathercli "Vasto, Italy"
```

---

## Options

```bash
weathercli --help
```

| Flag         | Description                          |
|--------------|--------------------------------------|
| `--compact`  | Minimal output                       |
| `--detailed` | Full weather details                 |
| `--f`        | Unit conversion to fahrenheit        |
| `--version`  | Show installed version               |

---

## Update

```bash
pipx upgrade weathercli
```

---

## Development
Be sure to install the requirements.txt when running locally
```bash
PYTHONPATH=src python -m weathercli.main "<location>"
```

Example:

```bash
PYTHONPATH=src python -m weathercli.main "Los Angeles, CA"
```

## Current Version **v1.0.3**

## Planned (v1.1.0)

- Unit selection (°C / °F)
- Weekly forecast
- More natural input handling

## Open Meteo Documentation
https://open-meteo.com/en/docs

## License MIT

