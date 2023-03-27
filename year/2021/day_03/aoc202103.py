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

def parse_string(puzzle_input):
    """[summary]

    Args:
        puzzle_input ([type]): [description]

    Returns:
        [type]: [description]
    """
    return [line for line in puzzle_input.split()]

def part_one(numbers):
    """[summary]

    Args:
        numbers ([type]): [description]
    """
    most_common = ''
    least_common = ''
    for i in range(len(numbers[0])):
        zeroes, ones = count_bits(numbers,i)
        if zeroes > ones:
            most_common += '0'
            least_common += '1'
        else:
            most_common += '1'
            least_common += '0'
    
    return int(most_common,2) * int(least_common,2)

def count_bits(numbers, col):
    freq_zero = 0
    freq_one = 0
    for line in range(len(numbers)):
        if numbers[line][col] == '0':
            freq_zero += 1
        else:
            freq_one += 1
    return freq_zero, freq_one

def part_two(numbers):
    """[summary]

    Args:
        numbers ([type]): [description]
    """
    #dict_zero, dict_one = find_bits(numbers)
    numbers_lsr = numbers[:]
    numbers_ogr = numbers[:]

    index = 0
    while len(numbers_lsr) > 1:
        zeroes, ones = count_bits(numbers_lsr,index)
        bit = '1' if ones >= zeroes else '0'
        numbers_lsr[:] = [x for x in numbers_lsr if x[index] == bit]
        index += 1

    index = 0
    while len(numbers_ogr) > 1:
        zeroes, ones = count_bits(numbers_ogr,index)
        bit = '0' if ones >= zeroes else '1'
        numbers_ogr[:] = [x for x in numbers_ogr if x[index] == bit]
        index += 1
    
    return int(numbers_lsr[0],2) * int(numbers_ogr[0],2)

def solve(puzzle_input):
    """[summary]

    Args:
        puzzle_input ([type]): [description]

    Returns:
        [type]: [description]
    """
    numbers = parse_string(puzzle_input)
    solution_1 = part_one(numbers)
    solution_2 = part_two(numbers)

    return solution_1,solution_2

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str,solutions)))
        