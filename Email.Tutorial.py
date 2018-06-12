import RPi.GPIO as GPIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)

msg = MIMEMultipart()
msg['From'] = ''
msg['To'] = ''
msg['Subject'] = 'PANIC!!!'
body = 'SOMEONE PRESSED THE BUTTON!!!'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('','')

while True:
    if GPIO.input(7) == 0:
        msg.attach(MIMEText(body, 'plain'))
        server.sendmail('','',msg.as_string())
