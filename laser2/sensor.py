# Implements a class to represent a laser sensor.

class LaserSensor:
	state = True
	spi = False
	port = 0
	level = 800
	value = 0;

	def __init__(self, port, spi, level = 800):
		self.port = port
		self.spi = spi
		self.level = level

	def getPort(self):
		return self.port

	def getState(self):
		self.checkState()
		return self.state

	def getValue(self):
		return self.value

	def checkState(self):
		self.value = self.readadc()
		if (self.value > self.level):
			# Laser On
			if not self.state:
				self.state = True
				return True
		else:
			# Laser Off
			if self.state:
				self.state = False
				return True

		return False


	# Read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
	def readadc(self):
		if not self.spi:
			return False

		# Read input from the chip and decode the value.    
		r = self.spi.xfer2([1, (8 + self.port) << 4, 0])
		adcout = ((r[1] & 3) << 8) + r[2]

		return adcout
