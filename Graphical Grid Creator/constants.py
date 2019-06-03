# Text size
T_BIG		= 100
T_MEDIUM	= 50
T_SMALL		= 25

# COLOR		  (  R,   G,   B)
WHITE		= (255, 255, 255)
BLACK		= (  0,   0,   0)
L_GRAY		= (200, 200, 200)
OV_L_GRAY	= (225, 225, 225)
M_GRAY		= (125, 125, 125)
OV_M_GRAY	= (150, 150, 150)
D_GRAY		= ( 50,  50,  50)
OV_D_GRAY	= ( 75,  75,  75)
BLUE		= (  0,   0, 255)
RED			= (255,   0,   0)

# color of different players

# french texts
# LANG_FR = {
# }

# english texts
LANG_EN = {
"CREDITS"		: (	"Grilles tournantes de Fleissner",
					"",
					"A project by",
					"",
					"Arthur Froger",
					"&",
					"Joshua Menanteau"),
"T_MAIN_MENU"	: ("Fleissner Grid editor",),
"T_SETTINGS"	: ("Choose The Grid Settings",),
"T_CHOOSE_MOD"	: ("Choose The Grid To Modifie",),
"T_CHOOSE_DEL"	: ("Choose The Grid To Delete",),
"T_CREDITS"		: ("Credits",),
"B_EXIT"		: "Exit",
"B_BACK"		: "Back",
"B_CREDITS"		: "Credits",
"B_CHOOSE_SET"	: "New Grid",
"B_CHOOSE_MOD"	: "Modifie Grid",
"B_NO_GRID"		: "Modifie Grid",
"B_NO_SPACE"	: "Save as new",
"B_START_EDIT"	: "Start",
"B_REPLACE"		: "Replace",
"B_SAVE_AS_NEW"	: "Save as new",
"B_CONFIRM"		: "Confirm",
"VB_GRID_SIZE"	: ("Grid size : ",),
}

# default general settings
DEFAULT = {
"HEIGHT"	: 720,
"WIDTH"		: 1280,
"LANG"		: LANG_EN
}

# RESOLUTION = [	[1280, 720], [1360, 768], [1600, 900],
# 				[1920, 1080], [2560, 1440], [3840, 2160]]

# limites for the number of player and dimension of the board
GAME_SETTINGS_LIMITE = ((4, 12),)

# var_type for var_button_c
GRID_SIZE = 0

# var_type for var_text_c
VAR_TYPE = {
}

VAR = {
}

# box disposition in grid selector
POSITION_720 = {
0			: (280, 280),
1			: ((640, 360),),
2			: ((495, 360), (785, 360)),
3			: ((350, 360), (640, 360), (930, 360)),
4			: (	(495, 215), (785, 215),
				(495, 505), (785, 505)),
5			: (	(495, 215), (785, 215),
				(350, 505), (640, 505), (930, 505)),
6			: (	(350, 215), (640, 215), (930, 215),
				(350, 505), (640, 505), (930, 505))
}

# grid_selector task
MOD = 0
DEL = 1

# legal name for .grid file
LEGAL_NAME = (	"grid_0.txt", "grid_1.txt", "grid_2.txt",
				"grid_3.txt", "grid_4.txt", "grid_5.txt")
