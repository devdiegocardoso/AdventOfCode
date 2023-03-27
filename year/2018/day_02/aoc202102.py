"""
[summary]
"""
import pathlib
import sys

def parse(puzzle_input):
    """[summary]

    Args:
        puzzle_input ([type]): [description]

    Returns:
        [type]: [description]
    """
    return [int(line) for line in puzzle_input.split()]

def parse_list(puzzle_input):
    """[summary]

    Args:
        puzzle_input ([type]): [description]

    Returns:
        [type]: [description]
    """
    list_tmp = [line for line in puzzle_input.split()]
    return [(list_tmp[i], int(list_tmp[i+1])) for i in range(0,len(list_tmp),2)]

def part_one(numbers):
    """[summary]

    Args:
        numbers ([type]): [description]
    """
    depth = 0
    position = 0
    for movement, units in numbers:
        if movement == 'forward':
            position += units
        elif movement == 'up':
            depth -= units
        else:
            depth += units
    return depth * position

def part_two(numbers):
    """[summary]

    Args:
        numbers ([type]): [description]
    """
    depth = 0
    position = 0
    aim = 0
    for movement, units in numbers:
        if movement == 'forward':
            position += units
            depth += aim * units
        elif movement == 'up':
            aim -= units
        else:
            aim += units
    return depth * position

def solve(puzzle_input):
    """[summary]

    Args:
        puzzle_input ([type]): [description]

    Returns:
        [type]: [description]
    """
    numbers = parse_list(puzzle_input)
    solution_1 = part_one(numbers)
    solution_2 = part_two(numbers)

    return solution_1,solution_2

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str,solutions)))
        