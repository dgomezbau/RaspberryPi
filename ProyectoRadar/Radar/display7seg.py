import RPi.GPIO as GPIO
import time

class Display:
    def __init__(self):
        self.LSBFIRST = 1
        self.MSBFIRST = 2
        self.dataPin = 5
        self.latchPin = 6
        self.clockPin = 13
        self.digitPin = (17,22,27,10)
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)    # Number GPIOs by its physical location
        GPIO.setup(self.dataPin, GPIO.OUT)       # Set pin mode to output
        GPIO.setup(self.latchPin, GPIO.OUT)
        GPIO.setup(self.clockPin, GPIO.OUT)
        for pin in self.digitPin:
            GPIO.setup(pin,GPIO.OUT)

    def shiftOut(self,dPin,cPin,order,val):      
        for i in range(0,8):
            GPIO.output(cPin,GPIO.LOW)
            if(order == self.LSBFIRST):
                GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
            elif(order == self.MSBFIRST):
                GPIO.output(dPin,(0x80&(val<<i)==0x80) and GPIO.HIGH or GPIO.LOW)
            GPIO.output(cPin,GPIO.HIGH)
            
    def outData(self,data):      #function used to output data for 74HC595
        GPIO.output(self.latchPin,GPIO.LOW)
        self.shiftOut(self.dataPin,self.clockPin,self.MSBFIRST,data)
        GPIO.output(self.latchPin,GPIO.HIGH)
        
    def selectDigit(self,digit): # Open one of the 7-segment display and close the remaining three, the parameter digit is optional for 1,2,4,8
        GPIO.output(self.digitPin[0],GPIO.LOW if ((digit&0x08) == 0x08) else GPIO.HIGH)
        GPIO.output(self.digitPin[1],GPIO.LOW if ((digit&0x04) == 0x04) else GPIO.HIGH)
        GPIO.output(self.digitPin[2],GPIO.LOW if ((digit&0x02) == 0x02) else GPIO.HIGH)
        GPIO.output(self.digitPin[3],GPIO.LOW if ((digit&0x01) == 0x01) else GPIO.HIGH)
    
    def display(self, distinput):   #display function for 7-segment display
        num = self.separadorNumeros(distinput)
        self.outData(0xff)   #eliminate residual display    
        self.selectDigit(0x08)   #Select the first, and display the single digit
        self.outData(num[3])
        time.sleep(0.003)   #display duration
    
        self.outData(0xff)
        self.selectDigit(0x04)   #Select the first, and display the single digit
        self.outData(num[2])
        time.sleep(0.003)   #display duration 
    
        self.outData(0xff)   #eliminate residual display    
        self.selectDigit(0x02)   #Select the first, and display the single digit
        self.outData(num[1])
        time.sleep(0.003)   #display duration
        
        self.outData(0xff)
        self.selectDigit(0x01)   #Select the first, and display the single digit
        self.outData(num[0])
        time.sleep(0.003)
        
    def numberDisplay(self, number):
        if(number == 0):
            return 0xc0 #192 in decimal
        if(number == 1):
            return 0xf9 #249 in decimal
        if(number == 2):
            return 0xa4 #164 in decimal
        if(number == 3):
            return 0xb0 #176 in decimal
        if(number == 4):
            return 0x99
        if(number == 5):
            return 0x92
        if(number == 6):
            return 0x82
        if(number == 7):
            return 0xf8
        if(number == 8):
            return 0x80
        if(number == 9):
            return 0x90

    def separadorNumeros(self, dist):
        distInt = int(dist)
        num = str(distInt)
        list_num = []
        listNumberInDisplay = []
        list_num.append(0)
        if(len(num) == 0):
            for i in range(4):
                list_num.append(0)            
        elif(len(num) == 1):
            list_num.append(0)
            list_num.append(0)
            for n in num:       
                n = int(n)
                list_num.append(n)
            
        elif(len(num) == 2):
            list_num.append(0)
            for n in num:       
                n = int(n)
                list_num.append(n)
        else:
            for n in num:       
                n = int(n)
                list_num.append(n)

        for n in list_num:        
            eachNumberInHexa = self.numberDisplay(n)
            listNumberInDisplay.append(eachNumberInHexa)
        return listNumberInDisplay

    def destroy(self):   # When "Ctrl+C" is pressed, the function is executed. 
        GPIO.cleanup()