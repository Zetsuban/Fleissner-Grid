from re import sub
from math import ceil,sqrt,floor
from random import randint,choice

from prints import *

# Convert the full sentence into cryptable sentence wuthout spaces or punctuations
def convertLetters(text):
	text = text.replace(" ","").lower()
	text = sub(r'[^\w\s]','',text)
	return text

# Complet the text string if it's too short wth random letterss
def completion(text, n):
	letters = "abcdefghijklmnopqrstuvwxyz"
	if n%2 == 1:
		while len(text) != (n*n) - 1:
			text += choice(letters)
		return text
	else:
		while len(text) != n*n:
			text += choice(letters)
		return text

# Rotates grid clockwise or counter clockise depending on clock
def rotation(grid, n, clock):
	return list(zip(*grid[::-1])) if clock == True else list(zip(*grid))[::-1]

# Checks if grid doesn't overlap when rotating
def correct(grid, n):
	pos = []
	rotations = 0
	while rotations < 4:
		for i in range(n):
			for j in range(n):
				if grid[i][j] == 1:
					pos.append([i,j])
		grid = rotation(grid, n, True)
		rotations += 1
	for k in pos:
		if pos.count(k) > 1:
			return False
	return  True

# Generate a random Fleissner grid if correct return false and/or user chose it
def randomGrid(n):
	grid = [[0] * n for i in range(n)]
	if n % 2 == 0:
		cellNb = (n*n) / 4
	else:
		cellNb = ((n*n)-1) / 4
	listCell = []
	
	while len(listCell) != cellNb:
		posY = randint(0,n-1)
		posX = randint(0,n-1)
		grid[posY][posX] = 1
		if ([posY,posX] not in listCell):
			if correct(grid,n):
				listCell.append([posY,posX])
			else:
				grid[posY][posX] = 0
	return grid

# Loads grid from file
def loadGrid(fileName="grid.txt"):
	grid = []
	with open(fileName) as f:
		data = f.read().split("\n")
	data.remove('')
	for line in data:
		grid.append(list(line))
	grid = [[int(i) for i in j] for j in grid]
	return grid

# Saves Grid to file
def saveGrid(grid, n, fileName="grid.txt"):
	with open(fileName, "w") as doc:
		for line in grid:
			for e in line:
				doc.write(str(e))
			doc.write("\n")
	print("\n\nThe grid has been succesfully saved to the", fileName, "file.")


# Crypts the text and returns it in a square
def cipher(grid, n, text, clock):
	square = [['0'] * n for i in range(n)]
	letter = 0
	listText = list(text)
	print(listText)
	rotationsNb = 0
	while rotationsNb < 4 or letter < len(listText):
		for j in range(n):
			for k in range(n):
				if grid[j][k] == 1:
					square[j][k] = listText[letter]
					letter += 1
		grid = rotation(grid, n, clock)
		rotationsNb += 1
	if n%2 == 1:
		square[floor(n/2)][floor(n/2)] = ""
	return square

# Converts the encrypted square into a string
def squareToText(square, n):
	cryptedText = ''
	for line in square:
		cryptedText += ''.join(line)
	return cryptedText


def cipherFleissner(grid, n, text, clock, fileName):
	text = completion(text,n)
	square = cipher(grid, n, text, clock)
	cryptedText = squareToText(square, n)

	# Displays the encypted text as it would show with the grid
	print("\n" * 200)
	print("This is the square as encrypted by the cipher :")
	display = ""
	print("_" * (n * 3 + 1))
	for i in range(n):
		display += "| "
		for j in range(n):
			display += square[i][j] + "  "
			if square[i][j] == "":
				display += " "
		display += "\n"
	print(display)

	print("Which makes the text become :\n", cryptedText)

	saveGrid(grid, n, fileName)
	input("Press enter to quit ...")

# Convert the input text into a two dimensionnal array
def textToSquare(text, n):
	lisText = list(text)
	letter = 0
	square = [[0] * n for i in range(n)]
	for j in range(n):
		for k in range(n):
			if n%2 == 1 and (j == floor(n/2) and k == floor(n/2)):
				square[j][k] = ""
			else:
				square[j][k] = lisText[letter]
				letter += 1
	print(square)
	return square

# Decrypts the squared text using the grid
def decipher(grid, n, square, clock):
	# clock = True if clock == False else False
	rotations = 0
	decrypted = ''
	while rotations < 4:
		for i in range(n):
			for j in range(n):
				if grid[i][j] == 1:
					decrypted += square[i][j]
		grid = rotation(grid, n, clock)
		rotations += 1
	return decrypted


def decipherFleissner(grid, n, text, clock):
	square = textToSquare(text, n)
	decrypted = decipher(grid, n, square, clock)
	print("\n" * 200, "The decrypted text according to the parameters you've entered is :\n", decrypted)

	input("\n\nPresse enter to exit . . .")



if __name__ == '__main__':

	print("\n" * 200)
	[print(line) for line in intro] # Introduction print
	mode = input()
	mode = 2 if mode == "2" else 1

	if mode == 1:
		print("\n" * 200)
		[print(line) for line in crypt]
		input("Presse enter to continue ...")

		print("\n" * 200)
		print("Do you want to use a randomly generated grid ? [y/N]")
		gener = input()
		gener = "y" if gener == "y" or gener == "Y" else "n"

		print("\n" * 200)
		[print(line) for line in rotation_print]
		clock = False if input() == "2" else True

		print("\n" * 200)
		print("Please enter the sentence you wish to encrypt.")
		text = convertLetters(input())

		n = ceil(sqrt(len(text)))

		print("\n" * 200)
		if gener == "y":
			grid = randomGrid(n)
			fileName = "grid.txt"
		else:
			[print(line) for line in fileName_print]
			fileName = input()
			if fileName == "":
				grid = loadGrid()
			else:
				if ".txt" not in fileName:
					fileName += ".txt"
				grid = loadGrid(fileName)
		if grid == False:
			[print(line) for line in error_file]
			quit()

		if correct(grid, n) == False:
			[print(line) for line in error_grid]
			quit()

		if len(text) > n*n:
			print("The grid that has been provided or generated will be too small to store this sentence, a new grid will be generated.")
			n = ceil(sqrt(len(text)))
			grid = randomGrid(n)

		cipherFleissner(grid, n, text, clock, fileName)


	elif mode == 2:
		print("\n" * 200)
		[print(line) for line in decrypt]
		input("Press enter to continue ...")

		[print(line) for line in fileName_print]
		fileName = input()
		if fileName == "":
			grid = loadGrid("grid.txt")
		else:
			if ".txt" not in fileName:
				fileName += ".txt"
			grid = loadGrid(fileName)
		if grid == False:
			[print(line) for line in error_file]
			quit()

		n = len(grid)

		if correct(grid, n) == False:
			[print(line) for line in error_grid]
			quit()

		print("\n" * 200)
		[print(line) for line in decrypt_clock]
		clock = False if input() == "2" else True

		print("\n" * 200)
		print("Please enter the sentence you wish to decrypt.")
		text = completion(convertLetters(input()), n)

		decipherFleissner(grid, n, text, clock)
