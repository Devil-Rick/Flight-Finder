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
        city_url = f"{self.url}/locations/query"
        city_params = {
            "term": city,
            "location_types": "city",
        }
        city_response = req.get(url=city_url, headers=self.header, params=city_params).json()
        return city_response["locations"][0]["code"]


test = FlightData()
test.search_city_code("Kolkata")  # returns IATA codes of city

# ------------------- OUTPUT Response ------------------- #
# {'locations': [{
#     'id': 'paris_fr',
#     'active': True,
#     'name': 'Paris',
#     'slug': 'paris-france',
#     'slug_en': 'paris-france',
#     'code': 'PAR',
#     'alternative_names': [],
#     'rank': 6,
#     'global_rank_dst': 3,
#     'dst_popularity_score': 5220602.0,
#     'timezone': 'Europe/Paris',
#     'population': 2138551,
#     'airports': 4,
#     'stations': 8,
#     'hotels': 3779,
#     'bus_stations': 11,.....
