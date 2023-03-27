import pathlib
import sys
def parse_list(puzzle_input):
    list_tmp = [line.split('|') for line in puzzle_input.split('\n')]


    return [
        {
            'patterns':pair[0].strip(),
            'output':pair[1].strip(),
            'count_outputs': [len(values) for values in pair[1].strip().split()]
        } for pair in list_tmp]

def has_sequence(output):
    return output in [2,4,3,7]

def part_one(numbers):
    return sum(1 for sequence in numbers for output in sequence['count_outputs'] if has_sequence(output))       

def find_numbers(sequence):
    display_found = {2:[],4:[]}
    for element in sequence:
        if len(element) in [2,4]:
            display_found[len(element)] = element
    return display_found

def evaluate_six(bits,display_one):
    for char in display_one:
        bits = bits.replace(char,'')
    return 6 if len(bits) == 5 else -1

def evaluate_nine(bits,display_four):
    for char in display_four:
        bits = bits.replace(char,'')
    return 9 if len(bits) == 2 else 0

def evaluate_three(bits,display_one):
    for char in display_one:
        bits = bits.replace(char,'')
    return 3 if len(bits) == 3 else -1


def evaluate_two(bits,display_four):
    for char in display_four:
        bits = bits.replace(char,'')
    return 2 if len(bits) == 3 else 5

def evaluate_number(numbers,bits:str):
    if len(bits) == 6:
        result = evaluate_six(bits[:],numbers[2])
        return result if result == 6 else evaluate_nine(bits[:],numbers[4])        
    result = evaluate_three(bits[:],numbers[2])
    return result if result == 3 else evaluate_two(bits[:],numbers[4])

def evaluate_display(bits):
    if len(bits) == 2:
        return 1
    elif len(bits) == 4:
        return 4
    elif len(bits) == 3:
        return 7
    elif len(bits) == 7:
        return 8
    return -1

def find_number(numbers,bits):
    result = evaluate_display(bits)
    return result if result != -1 else evaluate_number(numbers,bits)

def part_two(numbers):
    list_numbers = []
    for sequence in numbers:
        display = find_numbers(sequence['patterns'].split())
        number = []
        for output in sequence['output'].split():
            digit = find_number(display,output)
            number.append(digit)
        list_numbers.append(int(''.join(map(str,number))))
    return sum(list_numbers)

def solve(puzzle_input):
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
        