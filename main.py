import data_manager

dm = data_manager.DataManager()
sheet_data = dm.get_data()  # getting the present data in sheets
# dm.update_data(sheet_data)
dm.add_data(city="Mumbai", price=4000)
dm.print_data()