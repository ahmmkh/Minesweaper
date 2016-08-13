''' Classes for motors and car '''
import RPi.GPIO as GPIO 
class motor(object):
	"""docstring for motor"""
	def __init__(self, pinA,pinB,enableP):
		self.pinB = pinB
		self.pinA = pinA
		self.enableP =enableP
	def enable(self):
		GPIO.output(self.enableP,True)
	def disable(self):
		GPIO.output(self.enableP,False)	
	def control(self,command):
		command = command.lower()
		n1 = 0 if command in ['c','br'] else 0
		n2 = 0 if command in ['c','br'] else 1
		commanddic = {'f':-1,'b':0,'br':-1,'c':0}
		GPIO.output(self.pinA,n1-commanddic[command])
		GPIO.output(self.pinB,n2-commanddic[command])
class car(object):
	"""docstring for car"""
	def __init__(self, motorA,motorB):
		self.motorA = motorA
		self.motorB = motorB
	def control(self,com):
		cominv=com
		commands=(com,cominv)	
		commands = ('f','b') if com =='l' else ('b','f')
		self.motorA.enable()
		self.motorB.enable()
		self.motorA.control(commands[0])
		self.motorB.control(comands[1])

				
