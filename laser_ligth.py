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
L1 = 0;
L2 = 1;
L3 = 2;
L4 = 3;
L5 = 4;

# Configuration vars
LOWER = 500;

try:
	while True:
		v1 = readadc(L1);
		v2 = readadc(L2);
		v3 = readadc(L3);
		v4 = readadc(L4);
		v5 = readadc(L5);

		# Test light value
		print v1, ' - ', v2, ' - ', v3, ' - ', v4, ' - ', v5

		# hang out and do nothing for a half second
		time.sleep(.1);


except KeyboardInterrupt:
	GPIO.cleanup()
