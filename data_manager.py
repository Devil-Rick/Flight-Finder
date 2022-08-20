import config
import requests as req
import tabulate as tb
import flight_data


class DataManager:
    def __init__(self):
        self.key = config.SHEET_API_KEY
        self.price_url = f"{config.SHEET_APP_ID}/prices"
        self.user_url = f"{config.SHEET_APP_ID}/users"
        self.fl_data = flight_data.FlightData()
        self.header = {
            "Authorization": f"Bearer {self.key}"
        }

    def get_data(self):
        """
        :returns A list containing all the information our flight sheet.
        """
        sheet_get_response = req.get(self.price_url,
                                     headers=self.header).json()
        return sheet_get_response["prices"]

    def update_data(self, sheet_data):
        """
        Checks for the IATA codes for all the cities listed in the sheets
        and updates the req changes.
        """

        for data in sheet_data:
            city = data["city"]
            city_code = self.fl_data.search_city_code(city=city)
            if city_code != data['iataCode']:
                update_url = f"{self.price_url}/{data['id']}"
                update_params = {
                    "price": {
                        "iataCode": city_code
                    }
                }
                sheet_update = req.put(update_url,
                                       headers=self.header,
                                       json=update_params)
                sheet_update.raise_for_status()

    def print_data(self):
        """
        :return: Prints the data in a clean and presentable tabular format
        """

        data = self.get_data()
        header = data[0].keys()
        rows = [x.values() for x in data]
        print(tb.tabulate(rows, header))

    def add_data(self, price: int, city: str):
        """
        Let you add new places where you want to travel for your next trip planning
        :param price: Enter the max price under which Flights are to be searched
        :param city: Enter the city to which you want to travel
        """

        city_code = self.fl_data.search_city_code(city=city)
        add_params = {
            "price": {
                "city": city,
                "iataCode": city_code,
                "lowestPrice": price
            }
        }
        sheet_add = req.post(self.price_url,
                             headers=self.header,
                             json=add_params)
        sheet_add.raise_for_status()

    def add_user(self, first_name=None, last_name=None, email_id=None):
        if email_id is not None:
            mail_list = []
            add_params = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "emailId": email_id
                }
            }
            req.post(self.user_url, headers=self.header, json=add_params)
            users_list = req.get(self.user_url, headers=self.header).json()
            for user in users_list["users"]:
                mail_list.append(user["emailId"])
            return mail_list
