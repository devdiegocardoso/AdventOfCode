"""
[summary]
"""
import pathlib
import sys
from collections import defaultdict
from functools import reduce

def parse(puzzle_input):
    """
    Parse the puzzle input into a list of integers.

    Args:
        puzzle_input (str): The puzzle input to be parsed.

    Returns:
        list: A list of integers parsed from the puzzle input.
    """
    return list(puzzle_input.split('\n'))

def parse_list(puzzle_input):
    """
    Parse the puzzle input into a list of tuples.

    The puzzle input is expected to be a string containing pairs of values. 
    Each pair consists of a string followed by an integer. The function splits the input string, 
    converts the second value of each pair to an integer, and returns a list of tuples where the 
    first element of each tuple is the string and the second element is the corresponding integer.

    Args:
        puzzle_input (str): The puzzle input to be parsed.

    Returns:
        list: A list of tuples, where each tuple contains a string and an integer 
        parsed from the puzzle input.
    """

    list_tmp = list(puzzle_input.split())
    return [(list_tmp[i], int(list_tmp[i+1])) for i in range(0,len(list_tmp),2)]


def part_one(lines):
    """
    Calculate the solution for part one of the Advent of Code puzzle.

    This function takes a list of numbers as input and should return the solution 
    for part one of the puzzle. The specific behavior and implementation details 
    of this function are not provided in the code snippet.

    Args:
        numbers (list): A list of numbers.

    Returns:
        None: The function does not return any value.
    """
    dict_question = {"red":12,"green":13,"blue":14}
    total = 0
    for index,game in enumerate(lines,start=1):
        _, value = game.split(":")
        rounds = [value.strip() for value in value.split(";")]
        is_possible = True
        for cubes in rounds:
            cube_set = defaultdict(int)
            for cube in cubes.split(","):
                count, color = cube.split()
                cube_set[color] = int(count)
            for color in cube_set:
                if dict_question[color] < cube_set[color]:
                    is_possible = False
                    break
            if not is_possible:
                break
        if is_possible:
            total += index
    return total

def part_two(lines):
    """
    Calculate the solution for part two of the Advent of Code puzzle.

    This function takes a list of numbers as input and should return the solution for part two 
    of the puzzle. The specific behavior and implementation details of this function are not 
    provided in the code snippet.

    Args:
        numbers (list): A list of numbers.

    Returns:
        None: The function does not return any value.
    """
    total = 0
    for game in lines:
        dict_question = {"red":0,"green":0,"blue":0}
        _, value = game.split(":")
        rounds = [value.strip() for value in value.split(";")]
        for cubes in rounds:
            cube_set = defaultdict(int)
            for cube in cubes.split(","):
                count, color = cube.split()
                cube_set[color] = int(count)
            for color in cube_set:
                dict_question[color] = max(dict_question[color], cube_set[color])
        total += reduce(lambda a, b: a * b,dict_question.values())
    return total

def solve(puzzle_input):
    """
    Solve the Advent of Code puzzle.

    This function takes the puzzle input as input and returns the solutions for both 
    part one and part two of the puzzle. It first parses the puzzle input into a list 
    of numbers using the `parse` function. Then, it calculates the solution for part 
    one using the `part_one` function and the parsed numbers. Finally, it calculates 
    the solution for part two using the `part_two` function and the parsed numbers. 
    The solutions for both parts are returned as a tuple.

    Args:
        puzzle_input (str): The puzzle input to be solved.

    Returns:
        tuple: A tuple containing the solutions for part one 
        and part two of the puzzle, respectively.
    """

    lines = parse(puzzle_input)
    solution_1 = part_one(lines)
    solution_2 = part_two(lines)

    return solution_1,solution_2

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str,solutions)))
        