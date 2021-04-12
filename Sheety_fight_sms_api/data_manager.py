import requests
import os

SHEETY_URL = os.environ["sheety_url"]
HEADERS = {
    "Authorization" : os.environ["Authorization"]
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data_object = {}

    def get_data_google_doc(self):
        response = requests.get(SHEETY_URL, headers=HEADERS)
        data = response.json()
        return data

    def update_iataCode_google_doc(self):
        print(self.data_object["sheet1"])
        for row in self.data_object["sheet1"]:
            new_data = {
                "sheet1" : {
                    "iataCode" : row["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_URL}/{row['id']}",
                json=new_data,
                headers=HEADERS
            )
            print(response.text)
