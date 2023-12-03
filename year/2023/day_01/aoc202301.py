"""
[summary]
"""
import pathlib
import sys
import math


def parse(puzzle_input):
    """
    Parse the puzzle input into a list of integers.

    Args:
        puzzle_input (str): The puzzle input to be parsed.

    Returns:
        list: A list of integers parsed from the puzzle input.
    """
    return list(puzzle_input.split())

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

def find_first_digit(text):
    """
    Finds and returns the first digit in a given text.

    Args:
        text (str): The text to search for the first digit.

    Returns:
        str: The first digit found in the text.

    Examples:
        >>> find_first_digit("abc123")
        '1'
        >>> find_first_digit("def456")
        '4'
    """

    return next((character for character in text if character.isdigit()), "")

digits_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "1","2","3","4","5","6","7","8","9"]

def find_first_digit_with_letters(text, reverse=False):
    """
    Finds and returns the first digit in a given text.

    Args:
        text (str): The text to search for the first digit.

    Returns:
        str: The first digit found in the text.

    Examples:
        >>> find_first_digit("abc123")
        '1'
        >>> find_first_digit("def456")
        '4'
    """
    index_first = math.inf
    index_digit = -1
    for index,digit in enumerate(digits_letters):
        current_index = text.find(digit[::-1] if reverse else digit)
        if current_index < index_first and current_index != -1:
            index_first = current_index
            index_digit = index

    return digits_letters[index_digit if index_digit > 8 else index_digit + 9]

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
    sum_digits = 0
    for line in lines:
        first_digit,last_digit = find_first_digit(line),find_first_digit(line[::-1])
        sum_digits += int(first_digit + last_digit)

    return sum_digits

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
    sum_digits = 0
    for line in lines:
        first_digit,last_digit = find_first_digit_with_letters(line),find_first_digit_with_letters(line[::-1],True)
        sum_digits += int(first_digit + last_digit)
    

    return sum_digits

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
        