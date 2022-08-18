import config
import requests as req


class FlightData:
    def __init__(self):
        self.key = config.FLIGHT_API_KEY
        self.url = config.FLIGHT_URL  # (main website url)
        self.header = {
            "apikey": self.key
        }

    def search_city_code(self, city: str):
        """
        Searches and returns the city code for the city entered
        """

        city_url = f"{self.url}/locations/query"
        city_params = {
            "term": city,
            "location_types": "city",
        }
        city_response = req.get(url=city_url, headers=self.header, params=city_params).json()
        return city_response["locations"][0]["code"]

