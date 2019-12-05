from lirc import RawConnection
import RPi.GPIO as GPIO


LEDPIN1=4
LEDPIN2=25
LEDPIN3=24

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPIN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(LEDPIN2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(LEDPIN3, GPIO.OUT, initial=GPIO.HIGH)

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

setup()
while True:
    boton = ProcessIRRemote()
    if boton=='KEY_1':
        if GPIO.input(4)==1:  # returns 1
            print('Me enciendo')
            GPIO.output(LEDPIN1, GPIO.LOW)
        else:
            print('Me apago')
            GPIO.output(LEDPIN1, GPIO.HIGH)

    elif boton=='KEY_2':
        if GPIO.input(25)==1:  # returns 1
            print('Me enciendo')
            GPIO.output(LEDPIN2, GPIO.LOW)
        else:
            print('Me apago')
            GPIO.output(LEDPIN2, GPIO.HIGH)

    elif boton=='KEY_3':
        if GPIO.input(24)==1:  # returns 1
            print('Me enciendo')
            GPIO.output(LEDPIN3, GPIO.LOW)
        else:
            print('Me apago')
            GPIO.output(LEDPIN3, GPIO.HIGH) 