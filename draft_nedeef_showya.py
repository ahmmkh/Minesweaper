################# IMPORTS ################
import classes
import time
import serial
import RPi.GPIO as GPIO 
############## INTINALIZATION #############
rec = serial.Serial("/dev/ttyUSB0",9600,timeout=.1)
# - PINS ####################################
pins={"enableA":3,"pinA1":5,"pinA2": 7,"enableB":8,"pinB1" : 10,"pinB2": 12}
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# - pin setup ########################################
def setup():
	for i in pins.keys():
		GPIO.setup(pins[i],GPIO.OUT)
# -CAR AND MOTORS #####################################		
motarA = motar(pins['pinA1'],pins['pinA2'],pins['enableA'])
motarA = motar(pins['pinB1'],pins['pinB2'],pins['enableB'])
mine_car = car(motarA,motarB)
################## CONTROLS #######################
while True:
	msg = rec.read()
	mine_car.control(msg)




