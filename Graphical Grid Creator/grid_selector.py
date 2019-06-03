import pygame
import constants as c

class grid_selector_c(pygame.sprite.Sprite):

	def __init__(self, world, task):

		super().__init__()

		self.task = task
		self.names = world.saves
		self.clicked = -1

		self.grids = []
		for i in self.names:
			tmp_grid = []
			with open("grids/" + i, "r") as f:
				for line in f:
					tmp_line = []
					for char in line:
						if char == "0" or char == "1":
							tmp_line.append(int(char))
					tmp_grid.append(tmp_line)
			self.grids.append(tmp_grid)

		# boxes[x][0] : hit boxes of a grid
		# boxes[x][1] : is_overed
		self.boxes = [[pygame.Rect(	c.POSITION_720[len(self.names)][i],
									c.POSITION_720[0]), False]
									for i in range(0, len(self.names))]
		for i in range(0, len(self.names)):
			self.boxes[i][0].center = c.POSITION_720[len(self.names)][i]
		self.background	= pygame.Surface((	world.options["WIDTH"],
											world.options["HEIGHT"]),
											pygame.SRCALPHA)
		self.background.fill((0, 0, 0, 0))

		for i in range(0, len(self.names)):
			tmp_image = pygame.Surface(c.POSITION_720[0])
			tmp_image.fill(c.D_GRAY)
			for j in range(0, len(self.grids[i])):
				for k in range(0, len(self.grids[i])):
					if self.grids[i][j][k] == 1:
						pygame.draw.rect(tmp_image, c.M_GRAY,
										pygame.Rect(
											k * (280 / len(self.grids[i])),
											j * (280 / len(self.grids[i])),
											280 / len(self.grids[i]),
											280 / len(self.grids[i])))
			tmp_rect = tmp_image.get_rect()
			tmp_rect.center = c.POSITION_720[len(self.names)][i]
			self.background.blit(tmp_image, tmp_rect)

		self.image		= pygame.Surface((	world.options["WIDTH"],
											world.options["HEIGHT"]),
											pygame.SRCALPHA)
		self.image.fill((0, 0, 0, 0))
		self.rect = self.image.get_rect()
		# self.rect.centerx = world.options["WIDTH"]	/ 2
		# self.rect.centery = world.options["HEIGHT"]	/ 2

		self.draw(world)


	def update(self, world):

		mouse_pos	= pygame.mouse.get_pos()
		changed		= False
		old_clicked	= self.clicked

		for i in range(0, len(self.boxes)):
			self.boxes[i][1] = self.boxes[i][0].collidepoint(mouse_pos)
			if self.boxes[i][0].collidepoint(mouse_pos) and world.click:
				self.clicked = -1 if self.clicked == i else i
				if self.task == c.MOD:
					world.grid_name			= self.names[i]
					world.grid				= self.grids[i]
					world.game_set[0]	= len(self.grids[i])
				elif self.task == c.DEL:
					world.grid_name	= self.names[i]
			if self.boxes[i][1] or (old_clicked != self.clicked):
				changed = True

		if changed:
			self.draw(world)

	def draw(self, world):

		self.image.blit(self.background, self.rect)
		tmp_rect = pygame.Rect((0, 0), c.POSITION_720[0])
		for i in range(0, len(self.boxes)):
			if self.boxes[i][1]:
				tmp_rect.center = c.POSITION_720[len(self.names)][i]
				pygame.draw.rect(self.image, c.BLUE, tmp_rect, 1)
		if self.clicked != -1:
			tmp_rect.center = c.POSITION_720[len(self.names)][self.clicked]
			pygame.draw.rect(self.image, c.RED, tmp_rect, 1)
		# draw white square with low opacity on overed
		# draw red outline for selcted grids
