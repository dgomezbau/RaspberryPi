from lirc import RawConnection
import RPi.GPIO as GPIO
from encender import lcdOn
from apagar import lcdOff
from temhumsensor import getTemHum
from lightsensor import getAD



BUZZER = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(BUZZER, GPIO.OUT, initial = GPIO.HIGH)


def ProcessIRRemote():
       
    try:
        keypress = conn.readline(.0001) #lee la tecla pulsada
    except:
        keypress=""
              
    if (keypress != "" and keypress != None):
                
        data = keypress.split() #Separa los datos recibidos entre la cabecera y el numero del botón ( o identificación)
        #sequence = data[1]
        command = data[2]
        
        return command    
            

#define Global
conn = RawConnection()

print("Starting Up...")


def destroy():
    GPIO.output(BUZZER, GPIO.HIGH)
    GPIO.cleanup()

while True:
    try:
        boton = ProcessIRRemote()
        if boton=='KEY_1':
            lcdOn()

        elif boton=='KEY_2':
            lcdOff()

        elif boton=='KEY_3':
            getAD()

        elif boton=='KEY_4':
            if GPIO.input(BUZZER) == 1:
                GPIO.output(BUZZER, GPIO.LOW)
                print('open buzzer\n')
            else:
                GPIO.output(BUZZER, GPIO.HIGH)
                print('close buzzer\n')
            
        elif boton=='KEY_5':
            getTemHum()

    except KeyboardInterrupt:
        destroy()