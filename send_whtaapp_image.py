import os
from twilio.rest import Client

account_sid = 'AC713ee05b931d2914accbdf18245294a2'
auth_token  = '9814acfa3629028a9b5d81d8c7cecd6f'
client = Client(account_sid, auth_token)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+94763705333'

message = client.messages.create(body='Happey Be forver !',
                       media_url='https://source.unsplash.com/random/?productivity,Girl',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

print(message.sid)
