# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
# setup the parameters of the message
password = 'Eliminado por seguridad' #Introducir password
msg['From'] = 'daniel.gomez@movicoders.com'
msg['To'] = 'ignacio.claver@movicoders.com'
msg['Subject'] = 'Envio foto con Python'
 
# attach image to message body
filefoto = open('D:\\Curso Python MC\\RaspberryPi\\Hoja_09\\Ej_Extra\\fotoCarolDani.jpg', 'rb')
msg.attach(MIMEImage(filefoto.read()))

# attach text to message body
body = 'Buenas Ignacio,\nEjercicio extra de la hoja 9 by Carol & Dani'
msg.attach(MIMEText(body, 'plain'))
 
# create server
server = smtplib.SMTP('smtp.office365.com: 587')
 
server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
