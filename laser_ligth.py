#!/usr/bin/env python

import spidev
import RPi.GPIO as GPIO
import time
import os

# Set led pin.
GPIO.setmode(GPIO.BCM)
GREEN_LED = 24
GPIO.setup(GREEN_LED, GPIO.OUT)
 
spi = spidev.SpiDev()
spi.open(0,0)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
	r = spi.xfer2([1, (8 + adcnum) << 4, 0])
	adcout = ((r[1] & 3) << 8) + r[2]
	return adcout

# ADC ports (pins)
LIGHT_1 = 0;

# Configuration vars
LOWER = 500;

try:
	while True:
		value = readadc(LIGHT_1);
        	print "Light: ", "%d" % value;

		# Test light value
		if (LOWER < value ):
			GPIO.output(GREEN_LED, True)
		else:
			GPIO.output(GREEN_LED, False)

		# hang out and do nothing for a half second
		time.sleep(.1);


except KeyboardInterrupt:
	GPIO.cleanup()
