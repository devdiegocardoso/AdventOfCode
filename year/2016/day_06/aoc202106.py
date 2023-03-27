import pathlib
import sys
from collections import deque

def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split(',')]

def part_one(numbers):
    return find_total_fish(numbers,80)

def part_two(numbers):
    return find_total_fish(numbers,256)

def generate_fishes(timers,days):
    for _ in range(days):
        timers.rotate(-1)
        timers[6] += timers[8]

def initialize_deque(fishes):
    return deque([fishes.count(e) for e in range(9)])

def find_total_fish(fishes,days):
    timers = initialize_deque(fishes)
    generate_fishes(timers,days)
    return sum(timers)

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
        