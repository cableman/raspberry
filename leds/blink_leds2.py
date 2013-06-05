#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time

GPIO.setmode(GPIO.BCM)

GREEN_LED = 24
GPIO.setup(GREEN_LED, GPIO.OUT)

try:
	while True:

		GPIO.output(GREEN_LED, True)
		
		time.sleep(1)
		
		GPIO.output(GREEN_LED, False)

		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
