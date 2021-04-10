# # 4. Pass the data back to the main.py file, so that you can print the data from main.py
# from data_manager import DataManager
# data_manager = DataManager()
# sheet_data = data_manager.get_destination_data()
# # print(sheet_data)
#
# #  5. In main.py check if sheet_data contains any values for the "iataCode" key.
# #  If not, then the IATA Codes column is empty in the Google Sheet.
# #  In this case, pass each city name in sheet_data one-by-one
# #  to the FlightSearch class to get the corresponding IATA code
# #  for that city using the Flight Search API.
# #  You should use the code you get back to update the sheet_data dictionary.
# if sheet_data[0]["iataCode"] == "":
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code( row["city"] )
#     print(f"sheet_data:\n {sheet_data}")
#
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()

import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ffbdc6261c4539a63bff06621907c075/sheetySheet/sheet1"

headers = {
    "Authorization" : "Bearer banana"
}

sheety = requests.get(SHEETY_PRICES_ENDPOINT, headers=headers)
data = sheety.json()
print(data["sheet1"])

# new_data = {
#     "sheet1":{
#         "city" : "Bei Jing",
#         "lowestPrice": "800"
#     }
# }
#
# response = requests.put(
#     url=f"{SHEETY_PRICES_ENDPOINT}/11",
#     json=new_data
# )

# new_end_point = "https://api.sheety.co/ffbdc6261c4539a63bff06621907c075/sheetySheet/sheet1/10"
# response = requests.delete(new_end_point)



