#!/usr/bin/env python

import time
import os
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
DEBUG = 1
 
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
	if ((adcnum > 7) or (adcnum < 0)):
		return -1
	GPIO.output(cspin, True)
 
	GPIO.output(clockpin, False) # start clock low
	GPIO.output(cspin, False) # bring CS low
 
	commandout = adcnum
	commandout |= 0x18 # start bit + single-ended bit
	commandout <<= 3 # we only need to send 5 bits here
	for i in range(5):
		if (commandout & 0x80):
			GPIO.output(mosipin, True)
		else:
			GPIO.output(mosipin, False)
		commandout <<= 1
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)
 
	adcout = 0
	# read in one empty bit, one null bit and 10 ADC bits
	for i in range(12):
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)
		adcout <<= 1
		if (GPIO.input(misopin)):
			adcout |= 0x1
 
	GPIO.output(cspin, True)
	adcout >>= 1 # first bit is 'null' so drop it

	return adcout
 
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
 
# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
 
# TMP36 connected to adc #0
temp_adc = 0;

try:
	while True:
		value = readadc(temp_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
		mVolts = value * (3300.0 / 1024.0) 
		temp = ((mVolts - 100.0) / 10.0) - 40.0
 
		if DEBUG:
			print "Value: ", value
			print "MilliVolts: ", "%d" % mVolts
			
		print "Temperature: ", "%.1f" % temp
		print "\n"	

		# hang out and do nothing for a half second
		time.sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()
