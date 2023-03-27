import pathlib
import sys
from collections import Counter
from functools import reduce
def parse(puzzle_input):
    return [line for line in puzzle_input.split('\n')]

def count_vowels(entry):
    return Counter(letter for letter in entry if letter in 'aeiou')

def find_pair(entry):
    return any(entry[i] == entry[i+1] for i in range(len(entry)-1))

def find_sequence(entry,sequences):
    return any(sequence in entry for sequence in sequences)

def verify_conditions(entries):
    forbidden_pairs = ['ab','cd','pq','xy']
    nice = 0
    naughty = 0
    for entry in entries:
        has_all_properties = False
        has_forbidden_sequence = find_sequence(entry,forbidden_pairs)
        if not has_forbidden_sequence:
            total_vowels = sum(count_vowels(entry).values())
            if total_vowels >= 3:
                has_pair = find_pair(entry)
                if has_pair:
                    has_all_properties = True
        if has_all_properties:
            nice += 1
        else:
            naughty += 1
    return nice, naughty

def find_pairs_without_overlap(entry):
    c_dict = {}
    i_dict = {}
    for i in range(len(entry)-1):
        c_dict[(entry[i],entry[i+1])] = c_dict.get((entry[i],entry[i+1]),0)
        last_pair = i_dict.get((entry[i],entry[i+1]),(-1,-1))
        if last_pair == (-1, -1) or last_pair != (i - 1, i):
            i_dict[(entry[i],entry[i+1])] = (i,i+1)
            c_dict[(entry[i],entry[i+1])] += 1
    return any(value >= 2 for value in c_dict.values())

def find_equal_between_char(entry):
    return any(entry[i] == entry[i+2] for i in range(len(entry)-2))

def verify_new_conditions(entries):
    nice = 0
    for entry in entries:
        has_pair = find_pairs_without_overlap(entry)
        has_repeated_between_letters = find_equal_between_char(entry)
        if has_pair and has_repeated_between_letters:
            nice += 1
    return nice,0
def part_one(entries):
    nice, _ = verify_conditions(entries)
    return nice

def part_two(entries):
    nice, _ = verify_new_conditions(entries)
    return nice

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
        