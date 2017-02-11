import smtplib

from_addr = "julesingledew@gmail.com"
to_addr = "julian.i@live.com"
from_name = "Julian"
to_name = "Bob"
subject = "Kappa"
msg ="I'm 12 btw haHAA"


message = """
From: {} <{}>
To: {} <{}>

Subject: {}


{}
"""

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

#Credentials (if needed)
username = 'julesingledew@gmail.com'
password= 'xxxxxxxxxxxxxxxx'

#The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()