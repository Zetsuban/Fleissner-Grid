import pygame
from button			import button_c
from text_zone		import text_zone_c
from var_button		import var_button_c
from board			import board_c
from grid_selector	import grid_selector_c
from constants		import *

def main_menu(world):

	if world.all_object:
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	screen_center_y = world.options["HEIGHT"] / 2

	world.all_object.add(text_zone_c(world.options["LANG"]["T_MAIN_MENU"], BLUE,
		T_BIG, screen_center_x, T_BIG, "center"))
	j = 0
	for i in ("CHOOSE_SET", "CHOOSE_MOD" if len(world.saves) > 0 else "NO_GRID",
			"CREDITS", "EXIT"):
		world.all_object.add(button_c(world, world.options["LANG"]["B_" + i],
			BLUE, T_BIG, i, screen_center_x, screen_center_y + T_BIG * (j - 1)))
		j += 1

def game_settings(world):

	if world.all_object:
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	world.game_set[0] = 5
	world.grid = None
	screen_center_x = world.options["WIDTH"] / 2
	screen_center_y = world.options["HEIGHT"] / 2

	world.all_object.add(text_zone_c(world.options["LANG"]["T_SETTINGS"], BLUE,
		T_BIG, screen_center_x, T_BIG, "center"))
	world.all_object.add(text_zone_c(world.options["LANG"]["VB_GRID_SIZE"],
		BLUE, T_MEDIUM, screen_center_x, screen_center_y, "center"))
	world.all_object.add(var_button_c(WHITE, T_MEDIUM,
		screen_center_x + 150, screen_center_y, world.game_set[0], GRID_SIZE))
	world.all_object.add(button_c(world, world.options["LANG"]["B_START_EDIT"],
		BLUE, T_MEDIUM, "START", screen_center_x, screen_center_y + 100))
	world.all_object.add(button_c(world, world.options["LANG"]["B_BACK"], BLUE,
		T_MEDIUM, "BACK", screen_center_x, world.options["HEIGHT"] - T_BIG))
	# create text title/explenation
	# create var_button size
	# create button start_editor
	# create button back

def mod_grid_select(world):

	if world.all_object:
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	screen_center_y = world.options["HEIGHT"] / 2

	world.all_object.add(text_zone_c(world.options["LANG"]["T_CHOOSE_MOD"],
		BLUE, T_MEDIUM, screen_center_x, T_MEDIUM / 2, "center"))
	world.all_object.add(grid_selector_c(world, MOD))
	world.all_object.add(button_c(world, world.options["LANG"]["B_BACK"], BLUE,
		T_MEDIUM, "BACK",
		screen_center_x - 100, world.options["HEIGHT"] - T_MEDIUM / 2))
	world.all_object.add(button_c(world, world.options["LANG"]["B_CONFIRM"],
		BLUE, T_MEDIUM, "START",
		screen_center_x + 100, world.options["HEIGHT"] - T_MEDIUM / 2))
	# create chose box
	# create confirm button

def del_grid_select(world):

	if world.all_object:
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	screen_center_y = world.options["HEIGHT"] / 2

	world.all_object.add(text_zone_c(world.options["LANG"]["T_CHOOSE_DEL"],
		BLUE, T_MEDIUM, screen_center_x, T_MEDIUM / 2, "center"))
	world.all_object.add(grid_selector_c(world, DEL))
	world.all_object.add(button_c(world, world.options["LANG"]["B_BACK"], BLUE,
		T_MEDIUM, "START",
		screen_center_x - 100, world.options["HEIGHT"] - T_MEDIUM / 2))
	world.all_object.add(button_c(world, world.options["LANG"]["B_CONFIRM"],
		BLUE, T_MEDIUM, "SAVE_AS_NEW",
		screen_center_x + 100, world.options["HEIGHT"] - T_MEDIUM / 2))

def start_editor(world):

	if world.all_object:
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	screen_center_y = world.options["HEIGHT"] / 2

	if world.grid_name == None:
		for i in LEGAL_NAME:
			if i not in world.saves:
				world.grid_name = i
				break

	world.all_object.add(board_c(world, world.game_set[0], world.grid))

	j = 1
	for i in ("SAVE_AS_NEW" if len(world.saves) < len(LEGAL_NAME) else
			"NO_SPACE", "REPLACE"):
		world.all_object.add(button_c(world, world.options["LANG"]["B_" + i],
			BLUE, T_MEDIUM, i,
			world.options["HEIGHT"] - (T_MEDIUM * j), 0, "top_left"))
		j += 1

def save(world):

	if world.all_object:
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	with open("grids/" + world.grid_name, "w") as g:
		for i in world.grid:
			for j in i:
				g.write(str(j))
			g.write("\n")

	if not world.grid_name in world.saves:
		world.saves.append(world.grid_name)
	world.grid_name = None
	world.grid = None

	main_menu(world)

# doesn't do anything but do not delete
def dummy(world):
	pass

def credit(world):

	if world.all_object:
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	screen_center_y = world.options["HEIGHT"] / 2

	world.all_object.add(text_zone_c(world.options["LANG"]["T_CREDITS"], BLUE,
		T_BIG, screen_center_x, T_BIG, "center"))
	world.all_object.add(text_zone_c(world.options["LANG"]["CREDITS"], BLUE,
		T_MEDIUM, screen_center_x, screen_center_y, "center", "center"))
	world.all_object.add(button_c(world, world.options["LANG"]["B_BACK"], BLUE,
		T_BIG, "BACK", screen_center_x, world.options["HEIGHT"] - T_BIG))

def exit(world):
	world.running = False

B_FUNC = {
	"BACK"			: main_menu,
	"CHOOSE_SET"	: game_settings,
	"CHOOSE_MOD"	: mod_grid_select,
	"EXIT" 			: exit,
	"START" 		: start_editor,
	"SAVE_AS_NEW"	: save,
	"REPLACE"		: del_grid_select,
	"NO_GRID"		: dummy,
	"NO_SPACE"		: dummy,
	"CREDITS"		: credit
}
