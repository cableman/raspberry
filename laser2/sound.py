
# Import sound extension.
import pygame.mixer

class SoundPlayer:

	sounds = {
	  int('00000001', 2) : (lambda : pygame.mixer.Sound("./1.wav")),
	  int('00000010', 2) : (lambda : pygame.mixer.Sound("./2.wav")),
	  int('00000100', 2) : (lambda : pygame.mixer.Sound("./3.wav")),
	  int('00001000', 2) : (lambda : pygame.mixer.Sound("./4.wav")),
	  int('00010000', 2) : (lambda : pygame.mixer.Sound("./5.wav")),
	  int('00010001', 2) : (lambda : pygame.mixer.Sound("./6.wav"))
	}

	weight = [
		int('00010001', 2),
		int('00000001', 2),
		int('00000010', 2),
		int('00000100', 2),
		int('00001000', 2),
		int('00010000', 2)
	]

	def __init__(self):
		# Init mixer.
		pygame.mixer.init(44100, -16, 2, 1024)

		# Define sounds.
		s1 = pygame.mixer.Sound("./1.wav")

	def play(self, state):
		# Find the key to lookup (zeros is laser off eq play sound, so xor it)
		lookup = 0x1F ^ state

		#Based on the key find the first sound to match.
		for key in self.weight:
			if (key == lookup):
				self.sounds[key]().play()
				break;
