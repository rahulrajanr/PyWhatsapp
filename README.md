# PyWhatsapp
Python script to send notification via Whatsapp when a site goes down using Twilio API

export TWILIO_ACCOUNT_SID='ACxxxxxxxx' # paste in Account SID between single quotes

export TWILIO_AUTH_TOKEN='secret auth token' # paste Auth Token between single quotes

python3 -m venv pywhatsapp

sudo pip3 install virtualenv 

source ./pywhatsapp/bin/activate

pip3 install twilio

code
=======

from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+15005550006'

client.messages.create(body='Ahoy, world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
