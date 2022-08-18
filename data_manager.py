import config
import requests as req
import flight_data


class DataManager:
    def __init__(self):
        self.key = config.SHEET_API_KEY
        self.url = config.SHEET_APP_ID
        self.fl_data = flight_data.FlightData()
        self.header = {
            "Authorization": f"Bearer {self.key}"
        }

    def get_data(self):
        sheet_get_response = req.get(self.url,
                                     headers=self.header).json()
        return sheet_get_response["prices"]

    def update_data(self, sheet_data):
        for data in sheet_data:
            city = data["city"]
            city_code = self.fl_data.search_city_code(city=city)
            if city_code != data['iataCode']:
                update_url = f"{self.url}/{data['id']}"
                update_params = {
                    "price": {
                        "iataCode": city_code
                    }
                }
                sheet_update = req.put(update_url,
                                       headers=self.header,
                                       json=update_params)

    def add_data(self):
        pass


dm = DataManager()
sheet_data = dm.get_data()  # getting the present data in sheets
dm.update_data(sheet_data)

# ------------------- OUTPUT Response ------------------- #
# {'prices': [
#   {'city': 'Paris', 'iataCode': 'PHT', 'lowestPrice (indianRupees)': 40000, 'id': 2},
#   {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice (indianRupees)': 40000, 'id': 3},
#   {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice (indianRupees)': 40000, 'id': 4},
#   {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice (indianRupees)': 40000, 'id': 5},
#   {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice (indianRupees)': 40000, 'id': 6},
#   {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice (indianRupees)': 40000, 'id': 7},
#   {'city': 'New York', 'iataCode': 'NYS', 'lowestPrice (indianRupees)': 40000, 'id': 8},
#   {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice (indianRupees)': 40000, 'id': 9},
#   {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice (indianRupees)': 40000, 'id': 10}
#   ]
# }

