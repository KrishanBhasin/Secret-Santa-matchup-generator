
#TODO - automate the generation cyling
#TODO - generate more templates (gun, oscillator,LWSS etc)
#TODO - allow rotation of templates
#TODO - don't require knowledge of the board object in the methods of the cell object!

from tkinter import *
import time

class game:
	"""An object to store the game"""

	def __init__(self, size):
		self.size = size
		self.cell_size = 25
		window = Tk()
		self.canvas = Canvas(window, width=size * self.cell_size, height=size * self.cell_size)
		self.canvas.pack()

		self.board = [[cell(i, j) for i in range(size)] for j in range(size)]

		return None

	def drawbox(self):
		for j in range(self.size):
			for i in range(self.size):
				if self.board[i][j].alive:
					self.box_colour = "#220C65"
				else:
					self.box_colour = "#B7F3D5"
					
				self.canvas.create_rectangle(self.cell_size * i, self.cell_size * j,self.cell_size * i + self.cell_size,
				self.cell_size * j + self.cell_size, fill=self.box_colour, outline="#FFFFFF",width=2)

		return
		
	def countNeighbors(self,x,y):
		self.board[x][y].num_of_neighbors = 0
		for j in [-1, 0, 1]:
			for i in [-1, 0, 1]:
				if i == 0 and j == 0:	#avoid counting self
					continue
				elif (self.board[x][y].x + i) < 0 or (self.board[x][y].y + j < 0):	#avoid negative indexing
					continue
				try:
					if my_game.board[self.board[x][y].x + i][self.board[x][y].y + j].alive:	#increase count if living cell is found
						self.board[x][y].num_of_neighbors += 1
						continue
					else:	#ignore blank squares
						continue
				except IndexError:	#avoid IndexError from index too large
					continue

	def createGlider(self, x, y):
		self.board[x - 1][y - 1].alive = True
		self.board[x][y - 1].alive = True
		self.board[x + 1][y - 1].alive = True
		self.board[x + 1][y].alive = True
		self.board[x][y + 1].alive = True
		
	def createGun(self,x,y):
		self.board


class cell:
	"""An object for the cells in Conway's Game of Life"""

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.alive = False

	def livingCellCheck(self):
		if self.num_of_neighbors in [2,3]:
			self.alive = True
		else:
			self.alive = False


	def deadCellCheck(self):
		if self.num_of_neighbors == 3:
			self.alive = True
		else:
			self.alive = False

######################################################################################

if __name__ == "__main__":
	num_of_generations = int(input("How many generations do you wish to simulate?\n"))

	my_game = game(20)

	my_game.drawbox()

	my_game.board[1][1].alive = True
	my_game.board[1][2].alive = True
	my_game.board[2][2].alive = True


	my_game.createGlider(5, 10)
	my_game.drawbox()

	for _ in range(num_of_generations):
		for a in range(my_game.size):
			for b in range(my_game.size):
				my_game.countNeighbors(a,b)

		for a in range(my_game.size):
			for b in range(my_game.size):
				#print(my_game.board[a][b].num_of_neighbors)
				if my_game.board[a][b].alive:
					my_game.board[a][b].livingCellCheck()
				else:
					my_game.board[a][b].deadCellCheck()
		input()
		
		my_game.drawbox()


