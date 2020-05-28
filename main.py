def main():
	num, paths = __get_input()
	valleys = __check_valley(paths)

	print(valleys)

def __check_valley(paths):
	sea_level = 0
	valleys = 0

	for path in paths:
		if path == 'U':
			sea_level += 1
		elif path == 'D':
			if sea_level == 0:
				valleys += 1
			sea_level -= 1
	
	return valleys


def __get_input():
	num = input()
	paths = input()

	return num, paths

main()