import pathlib
import sys
from hashlib import md5

def parse(puzzle_input):
    return puzzle_input

def find_hex(sequence,start=1,prefix='00000'):
    number = start
    while True:
        mine_str = f'{sequence}{number}'
        digest = md5(mine_str.encode()).hexdigest()
        if digest.startswith(prefix):
            return number
        number += 1

def part_one(numbers):
    return find_hex(numbers)

def part_two(numbers,start):
    return find_hex(numbers,start,'000000')

def solve(puzzle_input):
    numbers = parse(puzzle_input)
    solution_1 = part_one(numbers)
    solution_2 = part_two(numbers,solution_1)

    return solution_1, solution_2


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str, solutions)))
