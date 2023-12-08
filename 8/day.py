import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from math import lcm

@timer
@print_result
def part1(input):
	d = {}

	instructions = input[0]
	for line in input[2:]:
		key, rest = line.split(" = ")
		left, right =  rest.split(", ")
		d[key] = (left[-3:], right[:3])

	
	li = len(instructions)
	steps = 0
	path = ["AAA"]
	while path[-1] != 'ZZZ':
		cur = path[-1]
		ins = instructions[steps % li]
		if ins == "L":
			path.append(d[cur][0])
		else:
			path.append(d[cur][1])
		steps += 1
	# print(path)
	return steps

@timer
@print_result
def part2(input):
	d = {}

	instructions = input[0]
	for line in input[2:]:
		key, rest = line.split(" = ")
		left, right =  rest.split(", ")
		d[key] = (left[-3:], right[:3])

	
	li = len(instructions)
	steps = 0

	stack = [i for i in d.keys() if i[-1] == "A"]
	fingerprints = []

	for key in stack:
		cur = key
		steps = 0
		fp = []

		while (cur, steps % li) not in fp:
			ins = instructions[steps % li]
			fp.append((cur, steps % li))
			if ins == "L":
				cur = d[cur][0]
			else:
				cur = d[cur][1]
			steps += 1
		# print(fp)
		fingerprints.append(fp)
		
	fps_i = []
	for fp in fingerprints:
		fp_i = []
		for i, val in enumerate(fp):	
			if val[0][-1] == 'Z':
				fp_i.append(i)
		fps_i.append(fp_i)


	# there was only one in each that had a Z in it
	out = 1
	for i in fps_i:
		out = lcm(out, i[0])
	return out



def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	if isinstance(input, str):
		part1(input)
		part2(input)
	else:
		part1(input.copy())
		part2(input.copy())

if __name__ == "__main__":
	main(argv[1:])
