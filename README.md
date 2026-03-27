```
    \  /          WEATHER CLI
  _ /"".-.        ───────────
    \_(   ).      Fast • Simple • Terminal Weather
    /(___(__)     Written By ChenchuH - 2026
      ‘ ‘ ‘ ‘
     ‘ ‘ ‘ ‘
```

## Usage

```weathercli <location>``` 

ex. ```weathercli Los Angeles, CA```

for assistance in using the tool 
```weatherclie -help```

## To run script

``` PYTHONPATH=src python -m weathercli.main ``` in bash once venv is activated - with cloned repo in project root

```pipx install "git+https://github.com/ChenchuH/WeatherCLI.git"``` to run as a CLI tool as intended, must have pipx installed prior

## To upgrade CLI tool
```pipx upgrade weathercli```

## pipx install (wsl/ubuntu)
```
sudo apt update
sudo apt install pipx
pipx ensurepath
```

verify install via 
``` pipx --version ```
### Planned 1.1.0 update
- units will start in C as default but upon further iterations, you will have the option to dictate units. 
- will create week forcast and more natural fetching language 
