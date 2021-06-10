def create_field(width: int = 3, height: int = 3, *args) -> list:
	field = []

	for space in  range(width * height):
		if space in args:
			field.append(1)
		else:
			field.append(0)
	
	return field


def tick(field: list, list_width: int) -> list:
	#alive_near = 0
	#for space in field:
	pass


def display_field(field:list) -> None:
	str_field = str(field)
	str_field = str_field.strip("[").strip("]")
	print(str_field)


if __name__ == "__main__":
	field = create_field(3,3, 2,7)
	display_field(field)


