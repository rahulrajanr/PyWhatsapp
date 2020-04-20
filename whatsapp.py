from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+919495278210'



import requests

urls = ['https://www.guru99.com',
 'https://www.tutorialspoint.com',
 'https://www.javatpoint.com',
 'https://ryanstutorials.net',
 'https://www.freecodecamp.org',
 'https://www.tecmint.com',
 'https://ubuntu.com',
 'https://linuxconfig.org',
 'https://linuxconfig.org',
 'https://www.howtoforge.com',
 'http://linuxcommand.org',
 'https://www.digitalocean.com',
 'http://www.yolinux.com',
 'https://maker.pro/linux',
 'https://www.computernetworkingnotes.com']


for url in urls:
    
    response = requests.get(url)
    
    if response.status_code == requests.codes.OK:
        
        print('{:35} - Ok'.format(url))
    
    else:
      client.messages.create(body=url + ' is down',from_=from_whatsapp_number,to=to_whatsapp_number)
