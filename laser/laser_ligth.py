#!/usr/bin/env python

import spidev
import RPi.GPIO as GPIO
import time
import os

import pygame.mixer

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

#sound files expect to be in the same directory as script
s1 = pygame.mixer.Sound("./1.wav")
s2 = pygame.mixer.Sound("./2.wav")
s3 = pygame.mixer.Sound("./3.wav")
s4 = pygame.mixer.Sound("./4.wav")
s5 = pygame.mixer.Sound("./5.wav")

pygame.mixer.init(44100, -16, 2, 1024)

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
		if (LOWER < v1 ):
			GPIO.output(GREEN_LED, True);
		else:
			GPIO.output(GREEN_LED, False);

		if (LOWER < v1):
			s1.play()
			
		if (LOWER < v2):
			s2.play()

		if (LOWER < v3):
			s3.play()

		if (LOWER < v4):
			s4.play()

		if (LOWER < v5):
			s5.play()

		# hang out and do nothing for a half second
		time.sleep(.1);


except KeyboardInterrupt:
	GPIO.cleanup();
