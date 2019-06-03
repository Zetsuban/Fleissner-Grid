import pygame
from pygame.locals import *
# import button_function as bf
from constants import *
import button_function as bf

class game_c():


	def __init__(self, options, saves):

		self.options	= options
		self.screen		= pygame.display.set_mode((	options["WIDTH"],
													options["HEIGHT"]))
		self.clock		= pygame.time.Clock()
		self.click		= False
		self.running	= True

		self.grid_name	= None
		self.game_set	= [5,]
		self.grid		= None

		self.saves		= saves

		self.all_object	= None
		self.background = pygame.Surface(self.screen.get_size())
		self.background.fill(BLACK)

	def event_loop(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.exit()
			if event.type == MOUSEBUTTONUP:
				self.click = True

	def world_loop(self):
		# bf.main_menu(self)
		self.all_object = pygame.sprite.Group()
		bf.main_menu(self)
		while self.running:
			self.screen.blit(self.background, (0, 0))
			self.event_loop()
			self.all_object.update(self)
			self.all_object.draw(self.screen)
			self.click = False
			pygame.display.flip()
			self.clock.tick(60)

	def exit(self):
		self.running = False
