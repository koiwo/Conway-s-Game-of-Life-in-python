class field:
	def __init__(self, width: int, height: int, filled_spaces: list = []):
		self.width = width
		self.height = height
		self.filled_spaces = filled_spaces
		self.layout = []


	def create_layout(self):
		for space in range(self.width * self.height):
			if space in self.filled_spaces:
				self.layout.append(1)
			else:
				self.layout.append(0)


	def next_state(self):
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



if __name__ == "__main__":
	a = field(4,4, [2,6,10])
	a.create_layout()
	print(a)
	for _ in range(7):
		a.next_state()
		print(a)
