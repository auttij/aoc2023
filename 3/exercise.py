import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import neighbors2d

@timer
@print_result
def exercise1(arr):
	line_len = len(arr[0])
	symbols = []
	numbers = []
	numpos = []

	for y, line in enumerate(arr):
		num = []
		num_loc = []
		for x, c in enumerate(line):
			if not c.isdigit() and c != '.':
				symbols.append((y, x))

			if c.isdigit():
				num.append(c)
				num_loc.append((y, x))
				if x == line_len - 1 or not line[x + 1].isdigit():
					numbers.append(int("".join(num)))
					num = []
					numpos.append(num_loc)
					num_loc = []

	out = []
	seen = []
	for pos in symbols:
		neis = tuple(neighbors2d(pos))
		for nei in neis:		
			for i, npos_arr in enumerate(numpos):
				if nei in npos_arr:
					if i not in seen:
						out.append(numbers[i])
						seen.append(i)
					
	return sum(out)

@timer
@print_result
def exercise2(arr):
	
	line_len = len(arr[0])
	symbols = []
	numbers = []
	numpos = []

	for y, line in enumerate(arr):
		num = []
		num_loc = []
		for x, c in enumerate(line):
			if c == '*':
				symbols.append((y, x))

			if c.isdigit():
				num.append(c)
				num_loc.append((y, x))
				if x == line_len - 1 or not line[x + 1].isdigit():
					numbers.append(int("".join(num)))
					num = []
					numpos.append(num_loc)
					num_loc = []

	out = {}
	for gi, pos in enumerate(symbols):
		neis = tuple(neighbors2d(pos))
		out[gi] = []

		for nei in neis:		
			for i, npos_arr in enumerate(numpos):
				if nei in npos_arr:
					if numbers[i] not in out[gi]:
						out[gi].append(numbers[i])
	
	ratio = 0
	for key, val in out.items():
		if len(val) == 2:
			ratio += val[0] * val[1]
	return ratio


def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
