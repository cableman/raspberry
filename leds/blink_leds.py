#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time

GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
BLUE_LED = 22

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

BTN = 25
GPIO.setup(BTN, GPIO.IN)

try:
	while True:

		GPIO.output(BLUE_LED, False)	
		GPIO.output(GREEN_LED, True)
		
		time.sleep(1)
		
		GPIO.output(GREEN_LED, False)
		GPIO.output(RED_LED, True)
		
		time.sleep(1)
			
		GPIO.output(RED_LED, False)
		GPIO.output(BLUE_LED, True)

		time.sleep(1)

		# If button pressed.
		if ( GPIO.input(25)== False ):
			# All leds on.
			GPIO.output(GREEN_LED, True)
			GPIO.output(RED_LED, True)
			GPIO.output(BLUE_LED, True)

			time.sleep(4)

			# All leds off.
			GPIO.output(GREEN_LED, False)
			GPIO.output(RED_LED, False)
			GPIO.output(BLUE_LED, False)

except KeyboardInterrupt:
	GPIO.cleanup()
