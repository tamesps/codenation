from main import get_temperature
from mock import Mock, patch

reponse = Mock()
reponse.json.return_value = {'currently': {'temperature': 62}}
mockapi = Mock()
mockapi.return_value = reponse


@patch('requests.get', mockapi)
def test_get_temperature_by_lat_lng():
    # setup
    expected = 16
    # verificação
    assert expected == get_temperature(-14.235004, -51.92528)
    # temperature = 62
