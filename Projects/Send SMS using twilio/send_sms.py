# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACf6eb21af513bc2f2b7d53dbb46e5e94e'
auth_token = '158366e7886efc16aca05fd8dc73a518'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is my first SMS through my python code.',
         from_='+13254138415',
         to='+447880313397'
     )

print(message.sid)
