import RPi.GPIO as GPIO
import time
from displayProcessing import separadorNumeros
 
LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 5    #DS Pin of 74HC595(Pin14)
latchPin  = 6      #ST_CP Pin of 74HC595(Pin12)
clockPin = 13       #SH_CP Pin of 74HC595(Pin11)
digitPin = (17,22,27,10)    # Define the pin of 7-segment display common end
 
def setup():
    GPIO.setmode(GPIO.BCM)    # Number GPIOs by its physical location
    GPIO.setup(dataPin, GPIO.OUT)       # Set pin mode to output
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    for pin in digitPin:
        GPIO.setup(pin,GPIO.OUT)
    
def shiftOut(dPin,cPin,order,val):      
    for i in range(0,8):
        GPIO.output(cPin,GPIO.LOW)
        if(order == LSBFIRST):
            GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin,(0x80&(val<<i)==0x80) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin,GPIO.HIGH)
            
def outData(data):      #function used to output data for 74HC595
    GPIO.output(latchPin,GPIO.LOW)
    shiftOut(dataPin,clockPin,MSBFIRST,data)
    GPIO.output(latchPin,GPIO.HIGH)
    
def selectDigit(digit): # Open one of the 7-segment display and close the remaining three, the parameter digit is optional for 1,2,4,8
    GPIO.output(digitPin[0],GPIO.LOW if ((digit&0x08) == 0x08) else GPIO.HIGH)
    GPIO.output(digitPin[1],GPIO.LOW if ((digit&0x04) == 0x04) else GPIO.HIGH)
    GPIO.output(digitPin[2],GPIO.LOW if ((digit&0x02) == 0x02) else GPIO.HIGH)
    GPIO.output(digitPin[3],GPIO.LOW if ((digit&0x01) == 0x01) else GPIO.HIGH)
 
def display(distinput):   #display function for 7-segment display
    num = separadorNumeros(distinput)
    outData(0xff)   #eliminate residual display    
    selectDigit(0x08)   #Select the first, and display the single digit
    outData(num[3])
    time.sleep(0.003)   #display duration
 
    outData(0xff)
    selectDigit(0x04)   #Select the first, and display the single digit
    outData(num[2])
    time.sleep(0.003)   #display duration 
 
    outData(0xff)   #eliminate residual display    
    selectDigit(0x02)   #Select the first, and display the single digit
    outData(num[1])
    time.sleep(0.003)   #display duration
    
    outData(0xff)
    selectDigit(0x01)   #Select the first, and display the single digit
    outData(num[0])
    time.sleep(0.003)
    

     
        
def destroy():   # When "Ctrl+C" is pressed, the function is executed. 
    GPIO.cleanup()      
 