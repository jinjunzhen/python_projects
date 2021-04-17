import os
from twilio.rest import Client
from dotenv import load_dotenv

## register on "https://www.twilio.com/" and get [account_sid] [auth_token] and [PHONE NUMBER]
load_dotenv()
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")


client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="CM， 起床啦～ 太阳晒屁股啦～ \n From jinjun zhen",
                     from_='+18508057664',
                     to='+14156082311'
                 )
print(message.sid)