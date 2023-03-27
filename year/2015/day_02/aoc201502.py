"""
[summary]
"""
import pathlib
import sys
from functools import reduce
def parse(puzzle_input):
    return [
        [int(dimensions) for dimensions in line.split('x')]
        for line in puzzle_input.split('\n')
    ]

def wrap(gifts):
    total_to_wrap = 0
    for gift in gifts:
        area_l_w = gift[0]*gift[1]
        area_w_h = gift[1]*gift[2]
        area_h_l = gift[2]*gift[0]
        values = [area_l_w,area_w_h,area_h_l]
        total_to_wrap += reduce(lambda x,y: x+y,map(lambda x: x*2,values)) + min(values)
    return total_to_wrap
    
def ribbon(gifts):
    total_to_ribbon = 0
    for gift in gifts:
        feet = gift[0]*gift[1]*gift[2]
        gift.remove(max(gift))
        total_to_ribbon += reduce(lambda x,y: x+y,map(lambda x: x * 2,gift)) + feet
    return total_to_ribbon

def part_one(numbers):
    return wrap(numbers)

def part_two(numbers):
    return ribbon(numbers)

def solve(puzzle_input):
    numbers = parse(puzzle_input)
    solution_1 = part_one(numbers)
    solution_2 = part_two(numbers)

    return solution_1,solution_2

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str,solutions)))
        