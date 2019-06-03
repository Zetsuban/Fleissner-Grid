import pygame
import constants		as c
# import button_function	as bf

class board_c(pygame.sprite.Sprite):

	def __init__(self, world, size, save = None):

		super().__init__()

		self.grid				= save if save else \
											[[0 for i in range(0, size)]
												for i in range(0, size)]
		self.size				= size
		if size % 2 != 0:
			self.grid[int(size / 2)][int(size / 2)] = -1

		self.image 				= pygame.Surface((	world.options["HEIGHT"],
												world.options["HEIGHT"]))
		self.rect				= self.image.get_rect()
		self.rect.centerx		= world.options["WIDTH"]  / 2
		self.rect.centery		= world.options["HEIGHT"] / 2

		# composed in such a way :
		# self.boxes[x][y] = [pygame.Rect, overed bool]
		# associated with self.grid[x][y]
		self.boxes	= [[[0, 0] for i in range(0, size)]
								for j in range(0, size)]
		boxes_size	= world.options["HEIGHT"] / size
		init_pos_x	= (world.options["HEIGHT"] - boxes_size * size) / 2
		init_pos_y	= (world.options["HEIGHT"] - boxes_size * size) / 2
		for i in range(0, size):		# go through rows
			for j in range(0, size):	# go through cols
				self.boxes[i][j] = [pygame.Rect((	init_pos_y + j * boxes_size,
													init_pos_x + i * boxes_size)
													, (boxes_size, boxes_size)),
									 False]

		world.grid = [[0 for i in range(0, size)] for i in range(0, size)]
		if save:
			for i in range(0, len(self.grid)):
				for j in range(0, len(self.grid)):
					if self.grid[i][j] == 1:
						rottated = get_rottated_pos(i, j, self.size - 1)
						for k in rottated:
							self.grid[k[0]][k[1]] = 2

		self.draw(world)

	def update(self, world):

		mouse_pos	= pygame.mouse.get_pos()
		changed		= False

		for i in self.boxes:
			for j in i:
				j[0].left += (world.options["WIDTH"] \
							- world.options["HEIGHT"]) / 2
				j[1] = j[0].collidepoint(mouse_pos)
				if j[1]:
					changed = True
				j[0].left -= (world.options["WIDTH"] \
							- world.options["HEIGHT"]) / 2

		if changed:
			self.grid_update(world)
			self.draw(world)

	def grid_update(self, world):

		for i in range(0, self.size):
			for j in range(0, self.size):
				if self.boxes[i][j][1] and world.click and self.grid[i][j] == 0:
					self.grid[i][j] = 1
					rottated = get_rottated_pos(i, j, self.size - 1)
					for k in rottated:
						self.grid[k[0]][k[1]] = 2
				elif self.boxes[i][j][1] and world.click \
						and self.grid[i][j] == 1:
					self.grid[i][j] = 0
					rottated = get_rottated_pos(i, j, self.size - 1)
					for k in rottated:
						self.grid[k[0]][k[1]] = 0

		for i in range(0, self.size):
			for j in range(0, self.size):
				if self.grid[i][j] == 1:
					world.grid[i][j] = 1
				else:
					world.grid[i][j] = 0

		# update case in self.grid
		# -1 for center
		# 0 for empty
		# 1 for hollowed
		# 2 for rottated hollowed

	def draw(self, world):

		for i in range(0, self.size):
			for j in range(0, self.size):
				box_img = pygame.Surface((self.boxes[i][j][0].width,
											self.boxes[i][j][0].height))
				if self.grid[i][j] == 0:
					box_img.fill(c.OV_D_GRAY if self.boxes[i][j][1] else c.D_GRAY)
				elif self.grid[i][j] == 1:
					box_img.fill(c.OV_M_GRAY if self.boxes[i][j][1] else c.M_GRAY)
				elif self.grid[i][j] == 2 or self.grid[i][j] == -1:
					box_img.fill(c.OV_L_GRAY if self.boxes[i][j][1] else c.L_GRAY)

				self.image.blit(box_img, self.boxes[i][j][0])

				if (self.grid[i][j] == 2 or self.grid[i][j] == -1) \
						and self.boxes[i][j][1]:
					pygame.draw.aaline(self.image, c.RED,
										self.boxes[i][j][0].topleft,
										self.boxes[i][j][0].bottomright, 3)
					pygame.draw.aaline(self.image, c.RED,
										self.boxes[i][j][0].topright,
										self.boxes[i][j][0].bottomleft, 3)

		# draw vertical sides of the boxes
		for i in range(0, self.size):
			pygame.draw.line(self.image,
							c.RED,
							self.boxes[0][i][0].topleft,
							self.boxes[-1][i][0].bottomleft, 3)
		pygame.draw.line(self.image, c.RED,
			self.boxes[0][-1][0].topright,
			self.boxes[-1][-1][0].bottomright, 3)

		# draw horizontal sides of the boxes
		for i in range(0, self.size):
			pygame.draw.line(self.image,
							c.RED,
							self.boxes[i][0][0].topleft,
							self.boxes[i][-1][0].topright, 3)
		pygame.draw.line(self.image, c.RED,
			self.boxes[-1][0][0].bottomleft,
			self.boxes[-1][-1][0].bottomright, 3)

def get_rottated_pos(pos_x, pos_y, size):
	rottated = [[pos_y			, size - pos_x],
				[size - pos_x	, size - pos_y],
				[size - pos_y	, pos_x]]
	return(rottated)
