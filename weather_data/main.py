from xml.etree import ElementTree

def get_slp(airport: str) -> float:
    """Get the sea level pressure for an airport.

    Args:
        airport (str): The airport code.

    Returns:
        float: The sea level pressure in hPa.
    """
    try:
        airport_metar = get_airport_data(airport)
        return float(airport_metar["sea_level_pressure_mb"])
    except Exception as ex:
        return ex

def get_airport_data(airport: str) -> dict:
    """Get the airport data for an airport.

    Args:
        airport (str): The airport code.

    Returns:
        dict: The airport data.
    """
    import requests
    result = requests.get(f"https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString={airport}&hoursBeforeNow=1")
    xml = ElementTree.fromstring(result.text)
    result = {child.tag: child.text if child.text != None else child.attrib for child in xml.findall("./data/METAR/*")}
    return result
