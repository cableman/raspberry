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
states = [True for i in range(4)]
pre_states = [True for i in range(4)]

# Function to init SPI.
def initSPI():
	spi = spidev.SpiDev()
	spi.open(0,0)

	return spi

# Start spi and init Sensors.
spi = initSPI()
sensors = [LaserSensor(port, spi, level) for port in range(4)]

# Init sound
#sounds = SoundPlayer()

try:
	while True:
		for sensor in sensors:
			if (sensor.changed()):
				states[sensor.getPort()] = sensor.getState()

		# Sound
		# hang out and do nothing for a half second
 		time.sleep(interval);

except KeyboardInterrupt:
	print 'Exiting'
