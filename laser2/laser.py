#!/usr/bin/env python

import time
import os

# Import SPI drivers.
import spidev


from sensor import LaserSensor
from sound import SoundPlayer

# Defind variables.
level = 100
interval = .1

# State vaiables (00011111 -> 31) in hex 1F.
state = 0x1F
last_state = 0x1F

# Function to init SPI.
def initSPI():
	spi = spidev.SpiDev()
	spi.open(0,0)

	return spi

# Start spi and init Sensors.
spi = initSPI()
sensors = [LaserSensor(port, spi, level) for port in range(4)]

# Init sound
player = SoundPlayer()

try:
	while True:
		state = 0x00		
		for sensor in sensors:
			if (sensor.getState()):
				# Laser on.
				state = state | (1 << sensor.getPort())

		# If any bits have been trun off (laser beam breaked).
		if ((0x1F ^ state) & last_state):
	     	# New sound should be played with the new state (if non change to off expression is false).
	     	#'{0:08b}'.format((int('00011111',2) ^ int('00011010', 2)) & int('00000111',2)) = '00000101'
	     	#	   						31					state               prev
			player.play(state)

		# Update state. 
		last_state = state

		# hang out and do nothing for a half second
		time.sleep(interval);

except KeyboardInterrupt:
	print 'Exiting...'
