from weathercli.helpers.weather_codes import wind_dir_helper, weather_dic_lookup


def test_wind_dir_helper_north():
    assert wind_dir_helper(0) == "N"


def test_wind_dir_helper_east():
    assert wind_dir_helper(90) == "E"


def test_weather_dic_lookup_clear_sky():
    fake_weather = {
        "current": {
            "weather_code": 0,
            "temperature_2m": 70,
            "apparent_temperature": 68,
            "wind_speed_10m": 10,
            "wind_gusts_10m": 15,
            "wind_direction_10m": 90,
            "relative_humidity_2m": 50,
            "time": "2026-03-30T12:00",
            "precipitation": 0,
            "snowfall": 0,
        },
        "current_units": {
            "temperature_2m": "F",
            "wind_speed_10m": "mph",
            "precipitation": "in",
            "snowfall": "in",
        },
    }

    result = weather_dic_lookup(fake_weather)

    assert result["code"] == 0
    assert result["desc"] == "Clear sky"
    assert result["temp"] == 70
    assert result["wind_dir"] == 90