#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from display import marcador
from display import lcd_byte
from display import ganador
from pitido import signal

buttonPinD = 26
buttonPinI = 27

LEDVerde = 24
LEDRojo = 23

pulsado = True

puntuacion_verde = 0
puntuacion_rojo = 0

def setup():
    global puntuacion_verde
    global puntuacion_rojo
    puntuacion_verde = 0
    puntuacion_rojo = 0
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDVerde,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(LEDRojo,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(buttonPinD,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.setup(buttonPinI,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(buttonPinD,GPIO.FALLING,callback = encenderLEDVerde)
    GPIO.add_event_detect(buttonPinI,GPIO.FALLING,callback = encenderLEDRojo)
    pass

def encenderLEDVerde(ev=None):
    global pulsado
    if pulsado:
        #El pin 6 corresponde al Buzzer
        if GPIO.input(6) == 1:
            GPIO.output(LEDVerde, GPIO.LOW)
            pulsado = False
        elif GPIO.input(6) == 0:
            GPIO.output(LEDRojo, GPIO.LOW)
            pulsado = False

def encenderLEDRojo(ev=None):
    global pulsado
    if pulsado:
        #El pin 6 corresponde al Buzzer
        if GPIO.input(6) == 1:
            GPIO.output(LEDRojo, GPIO.LOW)
            pulsado = False
        elif GPIO.input(6) == 0:
            GPIO.output(LEDVerde, GPIO.LOW)
            pulsado = False
        

def main():
    nombre1 = input("Nombre jugador 1: ")
    nombre2 = input("Nombre jugador 2: ")
    global pulsado
    global puntuacion_verde
    global puntuacion_rojo
    while (puntuacion_verde<5 and puntuacion_rojo<5):
        signal()
        if GPIO.input(24)==0:
            puntuacion_verde = puntuacion_verde + 1
            time.sleep(1)
            GPIO.output(LEDVerde, GPIO.HIGH)
            pulsado = True
            print('Punto para: ' + nombre1)
        elif GPIO.input(23)==0:
            puntuacion_rojo = puntuacion_rojo + 1
            time.sleep(1)
            GPIO.output(LEDRojo, GPIO.HIGH)
            pulsado = True
            print('Punto para: ' + nombre2)
        marcador(nombre1, nombre2, puntuacion_verde, puntuacion_rojo)
   
    if puntuacion_verde==5:
        GPIO.output(LEDVerde, GPIO.LOW)
        GPIO.output(LEDRojo, GPIO.HIGH)
        ganador(nombre1)

    else:
        GPIO.output(LEDRojo, GPIO.LOW)
        GPIO.output(LEDVerde, GPIO.HIGH)
        ganador(nombre2)


def destroy():
    GPIO.output(LEDVerde, GPIO.HIGH)
    GPIO.output(LEDRojo, GPIO.HIGH)
    GPIO.cleanup()
    lcd_byte(0x01, 0)

if __name__ == '__main__':
    setup()

    try:
        opcion = 'y'
        while opcion == 'y':
            main()
            opcion = input('¿Quieres jugar otra partida? (y/n): ')
        destroy()

    except KeyboardInterrupt:
        destroy()