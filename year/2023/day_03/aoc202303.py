"""
[summary]
"""
import pathlib
import sys
import re
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
    number_dict = defaultdict(list)
    symbol_dict = defaultdict(list)
    number_re = re.compile(r"([0-9]+)")
    symbol_re = re.compile(r"([^.0-9])")
    for index,line in enumerate(lines):
        #numbers = number_re.findall(line)
        for m in number_re.finditer(line):
            #print(m.start(),m.group())
            number_dict[index].append(((m.start(),m.end()),m.group()))
        for m in symbol_re.finditer(line):
            #print(m.start(),m.group())
            symbol_dict[index].append((m.start(),m.group()))
    return search_adjacencies(number_dict,symbol_dict,len(lines)-1)

def search_adjacencies(numbers,symbols,max_index):
    """
    Search for adjacent numbers in a given range based on symbols.

    Args:
        numbers (dict): A dictionary containing number keys and corresponding lists of numbers.
        symbols (list): A list of symbols.
        max_index (int): The maximum index value.

    Returns:
        int: The sum of the numbers found in the adjacent ranges.

    Examples:
        >>> numbers = {0: [(2, 3), (4, 5)], 1: [(1, 2), (3, 4)], 2: [(5, 6), (7, 8)]}
        >>> symbols = ['*', '#', '@', '&', '$']
        >>> max_index = 2
        >>> search_adjacencies(numbers, symbols, max_index)
        20
    """
    numbers_list = []
    for number_key in numbers:
        for number in numbers[number_key]:
            l_inf = 0 if number_key == 0 else number_key - 1
            l_sup = max_index if number_key == max_index else number_key + 2
            for i in range(l_inf, l_sup):
                for symbol in symbols[i]:
                    number_range,number_value = number[0],number[1]
                    symbol_position = symbol[0]
                    #print(symbol_position,number_range)
                    if symbol_position in range(number_range[0]-1,number_range[1]+1):
                        numbers_list.append(int(number_value))
    #print(numbers_list)
    return sum(numbers_list)

def search_adjacents_gears(numbers,symbols,max_index):
    """
    Search for adjacent numbers in a given range based on symbols.

    Args:
        numbers (dict): A dictionary containing number keys and corresponding lists of numbers.
        symbols (list): A list of symbols.
        max_index (int): The maximum index value.

    Returns:
        int: The sum of the numbers found in the adjacent ranges.

    Examples:
        >>> numbers = {0: [(2, 3), (4, 5)], 1: [(1, 2), (3, 4)], 2: [(5, 6), (7, 8)]}
        >>> symbols = ['*', '#', '@', '&', '$']
        >>> max_index = 2
        >>> search_adjacencies(numbers, symbols, max_index)
        20
    """
    numbers_list = []
    for symbol_key in symbols:
        for symbol in symbols[symbol_key]:
            l_inf = 0 if symbol_key == 0 else symbol_key - 1
            l_sup = max_index if symbol_key == max_index else symbol_key + 2
            n_gears_connections = []
            for i in range(l_inf, l_sup):
                for number in numbers[i]:
                    number_range,number_value = number[0],number[1]
                    symbol_position = symbol[0]
                    print(symbol_position,number_range)
                    if symbol_position in range(number_range[0]-1,number_range[1]+1):
                        n_gears_connections.append(int(number_value))
            if len(n_gears_connections) == 2:
                numbers_list.append(reduce(lambda x,y: x * y,n_gears_connections))
    #print(numbers_list)
    return sum(numbers_list)

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
    number_dict = defaultdict(list)
    symbol_dict = defaultdict(list)
    number_re = re.compile(r"([0-9]+)")
    symbol_re = re.compile(r"([*])")
    for index,line in enumerate(lines):
        #numbers = number_re.findall(line)
        for m in number_re.finditer(line):
            #print(m.start(),m.group())
            number_dict[index].append(((m.start(),m.end()),m.group()))
        for m in symbol_re.finditer(line):
            #print(m.start(),m.group())
            symbol_dict[index].append((m.start(),m.group()))
    return search_adjacents_gears(number_dict,symbol_dict,len(lines)-1)

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
        