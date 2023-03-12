import main as weather
import requests

def test_get_slp(monkeypatch):
    """Test the get_slp function."""

    monkeypatch.setattr(weather, "get_airport_data", lambda airport: {"sea_level_pressure_mb": 1016.0})
    result = weather.get_slp("CYYZ")
    assert result == 1016.0

def test_get_airport_data(monkeypatch):
    """Test the get_airport_data function."""
    # mock requests.get
    class MockResponse:
        def __init__(self, text):
            self.text = text
    monkeypatch.setattr(requests, "get", lambda url: MockResponse("""<?xml version="1.0" encoding="UTF-8"?>
<response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.2" xsi:noNamespaceSchemaLocation="http://www.aviationweather.gov/static/adds/schema/metar1_2.xsd">
  <request_index>150546311</request_index>
  <data_source name="metars" />
  <request type="retrieve" />
  <errors />
  <warnings />
  <time_taken_ms>3</time_taken_ms>
  <data num_results="1">
    <METAR>
      <raw_text>CYYZ 112000Z 31005KT 290V360 15SM BKN030 M01/M08 A3002 RMK SC7 SLP178</raw_text>
      <station_id>CYYZ</station_id>
      <observation_time>2023-03-11T20:00:00Z</observation_time>
      <latitude>43.67</latitude>
      <longitude>-79.62</longitude>
      <temp_c>-1.0</temp_c>
      <dewpoint_c>-8.0</dewpoint_c>
      <wind_dir_degrees>310</wind_dir_degrees>
      <wind_speed_kt>5</wind_speed_kt>
      <visibility_statute_mi>15.0</visibility_statute_mi>
      <altim_in_hg>30.02067</altim_in_hg>
      <sea_level_pressure_mb>1017.8</sea_level_pressure_mb>
      <sky_condition sky_cover="BKN" cloud_base_ft_agl="3000" />
      <flight_category>MVFR</flight_category>
      <metar_type>METAR</metar_type>
      <elevation_m>171.0</elevation_m>
    </METAR>
  </data>
</response>"""))

    result = weather.get_airport_data("CYYZ")

    expected = {
      "raw_text": "CYYZ 112000Z 31005KT 290V360 15SM BKN030 M01/M08 A3002 RMK SC7 SLP178",
      "station_id": "CYYZ",
      "observation_time": "2023-03-11T20:00:00Z",
      "latitude": "43.67",
      "longitude": "-79.62",
      "temp_c": "-1.0",
      "dewpoint_c": "-8.0",
      "wind_dir_degrees": "310",
      "wind_speed_kt": "5",
      "visibility_statute_mi": "15.0",
      "altim_in_hg": "30.02067",
      "sea_level_pressure_mb": "1017.8",
      "sky_condition": {"sky_cover":"BKN" , "cloud_base_ft_agl":"3000"},
      "flight_category": "MVFR",
      "metar_type": "METAR",
      "elevation_m": "171.0",
    }

    assert result == expected