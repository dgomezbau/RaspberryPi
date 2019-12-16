import RPi.GPIO as GPIO 
import time

class Rotation:

	def __init__(self, step):
		self.servoPin = 18
		self.setup()
		self.servo = GPIO.PWM(self.servoPin, 50)
		self.angle = 30
		self.step = step
		self.start(0)
		
	def setup(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.servoPin, GPIO.OUT)
		GPIO.output(self.servoPin, GPIO.LOW)
		
	def start(self, value):
		self.servo.start(value)

	def setAngle(self, newAngle):
		duty = newAngle / 18 + 2
		self.servo.ChangeDutyCycle(duty)
		#time.sleep(0.25)

	def cycleLeft(self):
		self.setAngle(self.angle)
		self.angle+=self.step

	def cycleRight(self):
		while self.angle>30:
			self.setAngle(self.angle)
			self.angle-=self.step

	
	def destroy(self):
		GPIO.output(self.servoPin, False)
		self.servo.ChangeDutyCycle(0)
		self.servo.stop()
		GPIO.cleanup()
	
	def getAngle(self):
		return self.angle