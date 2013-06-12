
# Import sound extension.
import pygame.mixer

class SoundPlayer:

	def __init__(self):
		# Init mixer.
		pygame.mixer.init(44100, -16, 2, 1024)

		# Define sounds.
		s1 = pygame.mixer.Sound("./1.wav")

	def play(self, values = []):
		s1.play()
