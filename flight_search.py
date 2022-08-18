import config
import requests as req
from datetime import date as dt
from dateutil.relativedelta import relativedelta


class FlightSearch:
    def __init__(self):
        self.key = config.FLIGHT_API_KEY
        self.url = config.FLIGHT_URL  # (main website url)
        self.header = {
            "apikey": self.key
        }
        self.from_date = (dt.today() + relativedelta(days=+1)).strftime("%d/%m/%Y")
        self.to_date = (dt.today() + relativedelta(days=+1, months=+6)).strftime("%d/%m/%Y")
        self.from_place = "CCU"

    def search_flight(self):
        search_url = f"{self.url}/v2/search"
        search_params = {
            "fly_from": self.from_place,
            "fly_to": "BOM",
            "date_from": self.from_date,
            "date_to": self.to_date,
            "adults": "1",
            "curr": "INR",
            "selected_cabins": "M",
            "limit": 3
        }
        search_response = req.get(url=search_url, headers=self.header,
                                  params=search_params)
        # print(search_response.json()["data"])
        for i in search_response.json()["data"]:
            print(i["price"], i["local_departure"])
            if i["price"] < 5000:
                print(i)


test = FlightSearch()
test.search_flight()

# ------------------ OUTPUT format ------------------- #
# {'search_id': 'c3f3a17f-7230-abb5-ded7-6d1e8b8da11a',
#      'currency': 'INR', 'fx_rate': 80.722724, 'data': [
#         {'id': '153804914b36000054410fd0_0',
#          'flyFrom': 'CCU', 'flyTo': 'BOM',
#          'cityFrom': 'Kolkata', 'cityCodeFrom': 'CCU',
#          'cityTo': 'Mumbai', 'cityCodeTo': 'BOM',
#          'countryFrom': {'code': 'IN', 'name': 'India'}, 'countryTo': {'code': 'IN', 'name': 'India'},
#          'distance': 1667.3,
#          'duration': {'departure': 10200, 'return': 0, 'total': 10200}, 'price': 11757,
#          'conversion': {'EUR': 145.64672, 'INR': 11757},
#          'fare': {'adults': 5878.5, 'children': 5878.5, 'infants': 5878.5}, 'bags_price': {'1': 0},
#          'baglimit': {'hand_height': 35, 'hand_length': 55, 'hand_weight': 7, 'hand_width': 25,
#                       'hold_dimensions_sum': 158, 'hold_height': 52, 'hold_length': 78, 'hold_weight': 15,
#                       'hold_width': 28}, 'availability': {'seats': 2}, 'airlines': ['G8'],
#
#                       'route': [
#             {'id': '153804914b36000054410fd0_0', 'combination_id': '153804914b36000054410fd0', 'flyFrom': 'CCU',
#              'flyTo': 'BOM', 'cityFrom': 'Kolkata', 'cityCodeFrom': 'CCU', 'cityTo': 'Mumbai', 'cityCodeTo': 'BOM',
#              'airline': 'G8', 'flight_no': 512, 'operating_carrier': 'G8', 'operating_flight_no': '512',
#              'fare_basis': '', 'fare_category': 'M', 'fare_classes': 'Z', 'fare_family': '', 'return': 0,
#              'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None,
#              'vehicle_type': 'aircraft', 'local_arrival': '2022-09-19T07:20:00.000Z',
#              'utc_arrival': '2022-09-19T01:50:00.000Z', 'local_departure': '2022-09-19T04:30:00.000Z',
#              'utc_departure': '2022-09-18T23:00:00.000Z'}],

#          'facilitated_booking_available': True,
#          'pnr_count': 1,
#          'has_airport_change': False,
#          'technical_stops': 0,
#          'throw_away_ticketing': False,
#          'hidden_city_ticketing': False,
#          'virtual_interlining': False,
#          'local_arrival': '2022-09-19T07:20:00.000Z',
#          'local_departure': '2022-09-19T04:30:00.000Z',
