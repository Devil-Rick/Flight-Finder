import data_manager
import flight_search as fl
import notification_manager as ntm

# -------------- Adds , views and updates our choice of flights --------------- #
dm = data_manager.DataManager()
sheet_data = dm.get_data()
dm.update_data(sheet_data)
dm.add_data(city="Mumbai", price=4000)
dm.print_data()

# -------------- Getting the info about flights --------------- #
get_flights = fl.FlightSearch()
flights_list = get_flights.search_flight(sheet_data)
get_flights.print_flights()

# -------------- Sending the flights list using email --------------- #
send_email = ntm.NotificationManager(flights_list)
