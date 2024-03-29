import pygame
import button_function

class button_c(pygame.sprite.Sprite):

	def __init__(	self, world, text, color, size, function,
					x, y, pos_type = "center"):

		super().__init__()

		self.color		= color
		self.function	= function
		self.overed		= False
		self.text		= text

		self.font	= pygame.font.SysFont(None, size)
		self.image	= self.font.render(text, True, color)
		self.rect	= self.image.get_rect()

		if self.function == "NO_GRID" or self.function == "NO_SPACE" or \
				((self.function == "REPLACE" or self.function == "SAVE_AS_NEW")
				and not is_save_legal(world)):
			self.over_in()

		if pos_type == "center":
			self.rect.centerx = x
			self.rect.centery = y
		elif pos_type == "top_left":
			self.rect.top	= x
			self.rect.left	= y

	def update(self, world):
		mouse_pos = pygame.mouse.get_pos()

		if ((self.function == "REPLACE" or self.function == "SAVE_AS_NEW")
				and not is_save_legal(world)) and not self.overed:
			self.over_in()
			self.overed = True
		elif ((self.function == "REPLACE" or self.function == "SAVE_AS_NEW")
				and is_save_legal(world)) and self.overed:
			self.over_out()
			self.overed = False

		if self.function != "NO_GRID" and self.function != "NO_SPACE" and \
				((self.function != "REPLACE" and self.function != "SAVE_AS_NEW")
				or is_save_legal(world)):
			if (self.rect.collidepoint(mouse_pos) and not self.overed):
				self.overed = True
				self.over_in()
			elif not self.rect.collidepoint(mouse_pos) and self.overed:
				self.overed = False
				self.over_out()
			if world.click and self.rect.collidepoint(mouse_pos):
				button_function.B_FUNC[self.function](world)

	def over_in(self):
		over_color = (	self.color[0] - 100 if self.color[0] - 100 >= 0 else 0 ,
						self.color[1] - 100 if self.color[1] - 100 >= 0 else 0 ,
						self.color[2] - 100 if self.color[2] - 100 >= 0 else 0 )
		self.image = self.font.render(self.text, True, over_color)

	def over_out(self):
		self.image = self.font.render(self.text, True, self.color)

def is_save_legal(world):
	for i in world.all_object.sprites():
		if "board_c" in str(i):
			for j in i.grid:
				if 0 in j:
					return(False)
			return(True)
	return(True)
