import requests
import os
SHEETY_PRICES_ENDPOINT = os.environ["sheety_url"]
headers = {
    "Authorization" : os.environ["sheety_token"]
}

############################################################################### get
# sheety = requests.get(SHEETY_PRICES_ENDPOINT, headers=headers)
# data = sheety.json()
# print(data["sheet1"])


############################################################################### put


# new_data = {
#     "sheet1":{
#         "city" : "Bei Jing",
#         "lowestPrice": "800"
#     }
# }
#
# response = requests.put(
#     url=f"{SHEETY_PRICES_ENDPOINT}/11",
#     json=new_data,
#     headers=headers,
# )
#
# print(response.text)


############################################################################### delete


response = requests.delete( url=f"{SHEETY_PRICES_ENDPOINT}/11", headers=headers)