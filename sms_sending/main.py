import os
from twilio.rest import Client

## register on "https://www.twilio.com/" and get [account_sid] [auth_token] and [PHONE NUMBER]
account_sid = "account_sid"
auth_token = "auth_token"


client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Yo, jjz. Havu you gotten a job yet?",
                     from_='+18508057664',
                     to='+14156082311'
                 )



print(message.sid)