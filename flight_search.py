import config
import requests as req
import tabulate as tb
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
        self.flight_result = []

    def search_flight(self, sheet_data):
        search_url = f"{self.url}/v2/search"
        for data in sheet_data:
            search_params = {
                "fly_from": self.from_place,
                "fly_to": data["iataCode"],
                "date_from": self.from_date,
                "date_to": self.to_date,
                "price_to": data["lowestPrice"],
                "adults": "1",
                "selected_cabins": "M",
            }

            response = req.get(url=search_url, headers=self.header,
                               params=search_params).json()["data"]
            if len(response) != 0:
                if len(response) <= 5:
                    self.update_flight(response, len(response))
                else:
                    self.update_flight(response, 5)
        return self.flight_result

    def update_flight(self, response, length):
        for flight in range(length):
            dep_date = response[flight]["local_departure"].split("T")[0]
            dep_time = response[flight]["local_departure"].split("T")[1].split(".")[0]
            ari_date = response[flight]["local_arrival"].split("T")[0]
            ari_time = response[flight]["local_arrival"].split("T")[1].split(".")[0]

            self.flight_result.append({"From": response[flight]["cityFrom"],
                                       "From Code": response[flight]["cityCodeFrom"],
                                       "To": response[flight]["cityTo"],
                                       "To Code": response[flight]["cityCodeTo"],
                                       "Departure Date": dep_date,
                                       "Departure Time": dep_time,
                                       "Arrival Date": ari_date,
                                       "Arrival Time": ari_time,
                                       "Price": response[flight]["price"],
                                       })

    def print_flights(self):
        """
            :return: Prints the data in a clean and presentable tabular format
        """
        data = self.flight_result
        header = data[0].keys()
        rows = [x.values() for x in data]
        print(tb.tabulate(rows, header))
