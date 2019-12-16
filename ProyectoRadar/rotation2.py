
import RPi.GPIO as GPIO
import time

class Rotation2:
    def __init__(self):

        self.OFFSE_DUTY = 0.5        #define pulse offset of servo
        self.SERVO_MIN_DUTY = 2.5+self.OFFSE_DUTY     #define pulse duty cycle for minimum angle of servo
        self.SERVO_MAX_DUTY = 12.5+self.OFFSE_DUTY    #define pulse duty cycle for maximum angle of servo
        self.servoPin = 18
        self.setup()
        self.angle = 30
        self.step = 2

    def map(self, value, fromLow, fromHigh, toLow, toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

    def setup(self):
        global p
        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        GPIO.setup(self.servoPin, GPIO.OUT)   # Set servoPin's mode is output
        GPIO.output(self.servoPin, GPIO.LOW)  # Set servoPin to low

        p = GPIO.PWM(self.servoPin, 50)     # set Frequece to 50Hz
        p.start(0)                     # Duty Cycle = 0
        
    def servoWrite(self, angle):      # make the servo rotate to specific angle (0-180 degrees) 
        if(angle<0):
            angle = 0
        elif(angle > 180):
            angle = 180
        p.ChangeDutyCycle(self.map(angle,0,180,self.SERVO_MIN_DUTY,self.SERVO_MAX_DUTY))#map the angle to duty cycle and output it
        
    def move(self):
            self.servoWrite(self.angle)
            self.angle = self.angle+self.step     # Write to servo
            time.sleep(1)

    def destroy(self):
        p.stop()
        GPIO.cleanup()

    def getAngle(self):
        return self.angle