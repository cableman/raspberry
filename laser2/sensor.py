# Implements a class to represent a laser sensor.

class LaserSensor:
	state = True
	spi = False
	port = 0
	level = 800

	def __init__(self, port, spi, level = 800):
		self.port = port
		self.state = active
		self.spi = spi
		self.level = level

	def getPort(self):
		return self.port

	def getState(self):
		return self.state

	# Read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
	def readadc(self):
	    if not spi:
			return False
		
		# Read input from the chip and decode the value.    
		r = spi.xfer2([1, (8 + self.port) << 4, 0])
		adcout = ((r[1] & 3) << 8) + r[2]

		return adcout
