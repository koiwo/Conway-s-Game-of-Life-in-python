import pygame
from pygame.locals import *
import time



class Field:
	def __init__(self, width: int, height: int, filled_spaces: list = []):
		self.width = width
		self.height = height
		self.filled_spaces = filled_spaces
		self.layout = []


	def get_layout(self):
		return list(self.layout)


	def get_width(self):
		return int(self.width)


	def get_height(self):
		return int(self.height)


	def create_layout(self):
		for space in range(self.width * self.height):
			if space in self.filled_spaces:
				self.layout.append(1)
			else:
				self.layout.append(0)


	def next(self):
		new_layout = []

		for index, space in enumerate(self.layout):
			alive_nearby = 0


			# checks the above three spaces
			if index >= self.width:
				if not (index + 1) % self.width:
					if self.layout[index-self.width - 1]:
						alive_nearby += 1
					if self.layout[index-self.width]:
						alive_nearby += 1

				elif not index % self.width:
					if self.layout[index-self.width]:
						alive_nearby += 1
					if self.layout[index-self.width + 1]:
						alive_nearby += 1

				else:
					if self.layout[index-self.width - 1]:
						alive_nearby += 1
					if self.layout[index-self.width]:
						alive_nearby += 1
					if self.layout[index-self.width + 1]:
						alive_nearby += 1


			#check the bottom three spaces
			if index < self.width * (self.height - 1):
				if not index % self.width:
					if self.layout[index+self.width]:
						alive_nearby += 1
					if self.layout[index+self.width + 1]:
						alive_nearby += 1

				elif not (index + 1) % self.width:
					if self.layout[index+self.width - 1]:
						alive_nearby += 1
					if self.layout[index+self.width]:
						alive_nearby += 1

				else:
					if self.layout[index+self.width - 1]:
						alive_nearby += 1
					if self.layout[index+self.width]:
						alive_nearby += 1
					if self.layout[index+self.width + 1]:
						alive_nearby += 1


			#check space to the right
			if (index + 1) % self.width:
				if self.layout[index+1]:
					alive_nearby += 1

			#check space to the left
			if index % self.width:
				if self.layout[index-1]:
					alive_nearby += 1


			if space:
				if alive_nearby < 2 or alive_nearby > 3:
					new_layout.append(0)
				elif alive_nearby == 2 or alive_nearby == 3:
					new_layout.append(1)
			else:
				if alive_nearby == 3:
					new_layout.append(1)
				else:
					new_layout.append(0)
		self.layout = new_layout
			


	def __repr__(self):
		new_width = self.width
		old_width =	0
		rows = []
		for i in range(self.height):

			rows.append(self.layout[old_width:new_width])
			old_width = new_width
			new_width = old_width + self.width

		table = ""
		for row in rows:
			table += str(row).strip("[").strip("]")
			table += "\n"
		return table


def main(game_field:Field) -> None:
	screen = pygame.display.set_mode((game_field.get_height()*10,game_field.get_width()*10))


	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
		x = 0
		y = 0


		for space in game_field.get_layout():
			if space:
				pygame.draw.rect(screen, (255,255,255), Rect(x, y, 10, 10))
		
			x += 10
			if x > game_field.get_width()*10-10:
				y += 10
				x = 0

		pygame.display.flip()
		game_field.next()
		time.sleep(0.1)
		screen.fill((0,0,0))



if __name__ == "__main__":
	pygame.init()
	pygame.display.set_caption("Conway's Game of Life")

	a = Field(100,100, [2,100,102,201,202,7980,7981,7982, 702.800,802,901,902])
	a.create_layout()

	main(a)
	pygame.quit()