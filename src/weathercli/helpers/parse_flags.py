import argparse

def parse_args():
    parser = argparse.ArgumentParser(prog="weathercli", description="Get current weather for any location from the terminal.")
    parser.add_argument("location", nargs="*", help="location to search")
    parser.add_argument("--version", action="store_true", help="show version")
    parser.add_argument("--detailed", action="store_true", help="includes humidity, windspeed and direction")
    parser.add_argument("--compact", action="store_true", help="includes only weather and percipitation")
    return parser.parse_args()
