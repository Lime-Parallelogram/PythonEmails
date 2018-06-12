import RPi.GPIO as GPIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)

msg = MIMEMultipart()
msg['From'] = 'raspberry11.250@gmail.com'
msg['To'] = 'will@44ld.co.uk'
msg['Subject'] = 'PANIC!!!'
body = 'SOMEONE PRESSED THE BUTTON!!!'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('raspberry11.250@gmail.com','Forest Gold')

while True:
    if GPIO.input(7) == 0:
        msg.attach(MIMEText(body, 'plain'))
        server.sendmail('raspberry11.250@gmail.com','will@44ld.co.uk',msg.as_string())
