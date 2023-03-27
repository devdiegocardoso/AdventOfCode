"""
[summary]
"""
import pathlib
import sys
from collections import Counter

def parse(puzzle_input):
    return {'entries': puzzle_input, 'counts':Counter(puzzle_input)}

def part_one(numbers):
    return numbers['counts']['('] - numbers['counts'][')']

def find_basement(entries):
    current_level = 0
    for index, entry in enumerate(entries,1):
        current_level += 1 if entry == '(' else -1
        if current_level == -1:
            return index
    return -1

def part_two(numbers):
    return find_basement(numbers['entries'])

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
        