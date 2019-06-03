import sys
import pygame
import os
from pygame.locals import *

import world as w
import constants as c

def main():

	game = w.game_c(c.DEFAULT, file_integrity_check())
	game.world_loop()

def file_integrity_check():

	digest = []

	print("starting file integrity check")
	for file_name in os.listdir("grids"):
		old_len_row = 0
		len_row = 0
		len_col = 0
		valid = True

		if file_name in c.LEGAL_NAME:
			with open("grids/" + file_name, "r") as f:
				for line in f:
					len_col += 1
					old_len_row = len_row if len_row != 0 else len(line) - 1
					len_row = len(line) - 1
					if not set(line) - set("\n") <= set("01") \
							or old_len_row != len_row:
						print(	"Warning : " + file_name +
							" is invalid (syntax error) and will be ingnored",
							file=sys.stderr)
						valid = False
						break;
				if valid and len_row == len_col:
					print(file_name + " is a valid file")
					digest.append(file_name)
				elif valid and len_row != len_col:
					print(	"Warning : " + file_name +
							" is invalid (not a square) and will be ingnored",
							file=sys.stderr)
		else:
			print(	"Warning : " + file_name +
					" has an invalid file name and will be ingnored",
					file=sys.stderr)
	print("ending file integrity check")


	return(digest)

if __name__ == '__main__':
	try:
		pygame.init()
		main()
		pygame.quit()
	except EOFError:
		sys.exit(-1)
	except KeyboardInterrupt:
		sys.exit(-1)
	else:
		sys.exit(0)
