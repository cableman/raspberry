#!/usr/bin/env python

import spidev
import time
import os
 
spi = spidev.SpiDev()
spi.open(0,0)

DEBUG = 1;

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
	r = spi.xfer2([1, (8 + adcnum) << 4, 0])
	adcout = ((r[1] & 3) << 8) + r[2]
	return adcout

# TMP36 connected to adc #0
temp_adc = 3;

try:
	while True:
		readadc(temp_adc)
		rawTemp = readadc(temp_adc)
		milliVolts = rawTemp * (3300.0 / 1024.0)
        	tempCelsius = ((milliVolts - 100.0) / 10.0) - 40.0
 
		if DEBUG:
			print "Value: ", rawTemp
			print "MilliVolts: ", "%d" % milliVolts
			
		print "Temperature: ", "%4.1fC" % tempCelsius
		print "\n"	

		# hang out and do nothing for a half second
		time.sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()
