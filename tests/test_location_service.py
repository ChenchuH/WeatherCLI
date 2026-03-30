from unittest.mock import patch, Mock
from weathercli.helpers.location_service import get_location_data


@patch("weathercli.helpers.location_service.geolocator.geocode")
def test_get_location_data_success(mock_geocode):
    fake_location = Mock()
    fake_location.latitude = 33.8358
    fake_location.longitude = -118.3406
    mock_geocode.return_value = fake_location

    result = get_location_data("Torrance, CA")

    assert result == (33.8358, -118.3406)


@patch("weathercli.helpers.location_service.geolocator.geocode")
def test_get_location_data_invalid_location(mock_geocode):
    mock_geocode.return_value = None

    result = get_location_data("not-a-real-place-123")

    assert result is None


@patch("weathercli.helpers.location_service.geolocator.geocode")
def test_get_location_data_exception(mock_geocode):
    mock_geocode.side_effect = Exception("geocode failed")

    result = get_location_data("Torrance, CA")

    assert result is None