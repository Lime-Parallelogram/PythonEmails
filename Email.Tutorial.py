#Imports modules
import RPi.GPIO as GPIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Sets up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)

#Sets up msg variable with email info
msg = MIMEMultipart()
msg['From'] = 'from email' #Email you are sending from (most email clients don't look at this detail)
msg['To'] = 'to email' #Email sending to
msg['Subject'] = 'PANIC!!!' #Email subject
body = 'SOMEONE PRESSED THE BUTTON!!!' #Email content

server = smtplib.SMTP('smtp.gmail.com', 587) #Mail server (gmail) and port (gmail)
server.ehlo()
server.starttls() #Encryption
server.login('email','password') #Your login details (Google account if you are using gmail like me)

while True:
    if GPIO.input(7) == 0: #When the pin is pulled low by the button
        msg.attach(MIMEText(body, 'plain')) #Adds the body onto the other deatails
        server.sendmail('from email','to email',msg.as_string()) #Sends emails
