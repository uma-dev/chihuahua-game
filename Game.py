import pygame
from GeneralInformation import SKY_BLUE, SIZE
from Entities.Entities import Character

size = SIZE
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dogs")

class Game(object):
	def __init__(self):
		self.running = True #logic
		self.clock = pygame.time.Clock() #clock
		self.drawable_sprites = pygame.sprite.Group() #initial position
		self.character = Character(screen, (size[0]/2) , -100) #
		self.drawable_sprites.add(self.character)

	def keydown(self, event_key):
		self.character.key_down(event_key)

	def keyup(self, event_key):
		self.character.key_up(event_key)

	def runGame(self):

		while(self.running):
			screen.fill(SKY_BLUE)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

				if event.type == pygame.KEYDOWN:
					self.keydown(event.key)
				if event.type == pygame.KEYUP:
					self.keyup(event.key)

			dt = self.clock.tick(50)

			self.character.update(dt)

			for sprite in self.drawable_sprites.sprites():
				sprite.draw()

			pygame.display.update()
		pygame.quit()

if __name__=="__main__":
	game = Game()
	game.runGame()
