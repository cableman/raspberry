
# Import sound extension.
import time
import pygame.mixer

class SoundPlayer:

	sound = False

	sounds = {
	  int('00000001', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/open.wav")),
	  int('00000010', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/data.wav")),
	  int('00000100', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/bar.wav")),
	  int('00001000', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/library.wav")),
	  int('00010000', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/source.wav")),
	  int('00011111', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/superman.wav")),
	  int('00000011', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/open_data.wav")),
	  int('00000110', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/open_source.wav")),
	  int('00001100', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/open_bar.wav")),
	  int('00011000', 2) : (lambda : pygame.mixer.Sound("/root/laser2/sound/d_and_g.wav")),
	}

	weight = [
		int('00011111', 2),
		int('00000011', 2),
		int('00000110', 2),
		int('00001100', 2),
		int('00011000', 2),
		int('00000001', 2),
		int('00000010', 2),
		int('00000100', 2),
		int('00001000', 2),
		int('00010000', 2),
	]

	def __init__(self):
		# Init mixer.
		pygame.mixer.init(44100, -16, 2, 1024)
		self.sound = pygame.mixer.Sound("./sound/superman.wav")

	def play(self, state):
		# Find the key to lookup (zeros is laser off eq play sound, so xor it)
		lookup = 0x1F ^ state

		#Based on the key find the first sound to match.
		for key in self.weight:
			if (key == lookup):
				if (self.sound.get_length() > 2):
					self.sound.stop()
				# Play sound and block to done.
				self.sound = self.sounds[key]()
				self.sound.play()
				if (self.sound.get_length() < 2):
					time.sleep(self.sound.get_length())
				break;
