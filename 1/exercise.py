import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	a = []
	for line in arr:
		asd = []
		for char in line:
			if char.isnumeric():
				asd.append(char)
		a.append(int(asd[0] + asd[-1], 10))
	return sum(a)

@timer
@print_result
def exercise2(arr):
	arr2 = []
	for j, line in enumerate(arr):
		digits = []

		for i, char in enumerate(line):
			if char.isdigit():
				digits.append(char)
			for d, num in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
				if line[i:].startswith(num):
					digits.append(str(d))
		arr2.append(int(digits[0] + digits[-1], 10))
	return sum(arr2)


def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise2(arr)

if __name__ == "__main__":
	main(argv[1:])
