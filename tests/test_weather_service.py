from unittest.mock import Mock, patch
from weathercli.helpers.weather_service import get_weather_data


@patch("weathercli.helpers.weather_service.requests.get")
def test_get_weather_data_success(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "current": {
            "temperature_2m": 72
        }
    }
    mock_get.return_value = mock_response

    data = get_weather_data(33.8, -118.3)

    assert data["current"]["temperature_2m"] == 72


@patch("weathercli.helpers.weather_service.requests.get")
def test_get_weather_data_returns_none_on_error(mock_get):
    mock_get.side_effect = Exception("network error")

    data = get_weather_data(33.8, -118.3)

    assert data is None