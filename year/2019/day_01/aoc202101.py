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

def part_one(numbers):
    """[summary]

    Args:
        numbers ([type]): [description]

    Returns:
        [type]: [description]
    """
    measurements = numbers
    return sum(
        measurements[i] > measurements[i - 1] for i in range(1, len(measurements))
    )

def part_two(numbers):
    """[summary]

    Args:
        numbers ([type]): [description]

    Returns:
        [type]: [description]
    """
    measurements = numbers
    window = [sum(measurements[i:i+3]) for i in range(len(measurements)) if i < len(measurements)-2]

    return sum(
        window[i] > window[i - 1] for i in range(1, len(window))
    )

def solve(puzzle_input):
    """[summary]

    Args:
        puzzle_input ([type]): [description]

    Returns:
        [type]: [description]
    """
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
        