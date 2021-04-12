#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch


data_case = DataManager()
flight_search = FlightSearch()
my_data = data_case.get_data_google_doc()


for row in my_data["sheet1"]:
    if row["iataCode"] == "":
        row["iataCode"] = "fill in here"

data_case.data_object = my_data
data_case.update_iataCode_google_doc()