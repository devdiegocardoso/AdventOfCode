import pathlib
import sys

def parse(puzzle_input):
    return [line for line in puzzle_input.split('\n')]

def find_open_char(character):
    if character == ')':
        return '('
    elif character == '}':
        return '{'
    elif character == ']':
        return '['
    elif character == '>':
        return '<'
    return None

def find_close_char(character):
    if character == '(':
        return ')'
    elif character == '{':
        return '}'
    elif character == '[':
        return ']'
    elif character == '<':
        return '>'
    return None

def verify_corruption_value(item):
    if item == ')':
        return 3
    elif item == ']':
        return 57
    elif item == '}':
        return 1197
    elif item == '>':
        return 25137

def verify_incomplete_value(item):
    if item == ')':
        return 1
    elif item == ']':
        return 2
    elif item == '}':
        return 3
    elif item == '>':
        return 4

def calculate_corruption_level(corrupted_list):
    return sum(verify_corruption_value(item) for item in corrupted_list)


def part_one(entry):
    open_characters = "{(<["
    corrupt_characters = []
    incomplete_sequence = []
    for element in entry:
        stack = []
        corrupted_sequence = False
        for character in element:
            if character in open_characters:
                stack.append(character)
            else:
                open_char = find_open_char(character)
                stacked_char = stack.pop()
                if open_char != stacked_char:
                    corrupted_sequence = True
                    corrupt_characters.append(character)
                    break
        if not corrupted_sequence:
            incomplete_sequence.append(stack)
    return calculate_corruption_level(corrupt_characters), incomplete_sequence

def calculate_complete_score(sequence):
    score = 0
    for item in sequence:
        weight = verify_incomplete_value(item)
        score = (score*5) + weight
    return score

def part_two(entry):
    scores = []
    for element in entry:
        close_characters = [find_close_char(character) for character in reversed(element)]
        scores.append(calculate_complete_score(close_characters))
    middle_score = len(scores)//2
    return sorted(scores)[middle_score]

def solve(puzzle_input):
    entry = parse(puzzle_input)
    solution_1, incomplete = part_one(entry)
    solution_2 = part_two(incomplete)

    return solution_1,solution_2

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str,solutions)))