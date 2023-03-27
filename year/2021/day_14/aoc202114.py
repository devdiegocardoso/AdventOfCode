import pathlib
import sys
from collections import Counter
from copy import deepcopy

def parse(puzzle_input):
    list_tmp = [line for line in puzzle_input.split('\n')]
    dict_data = {'template': list_tmp.pop(0),'rules':{}}
    list_tmp.pop(0)
    for item in list_tmp:
        key, value = item.split(' -> ')
        dict_data['rules'][key] = value
    return dict_data
   

def create_polymer_optimized(rules,group_sequences):
    pairs = [(pair,group_sequences[pair]) for pair in group_sequences if group_sequences[(pair[0],pair[1])] > 0]
    new_counter = {}
    for pair, counter in pairs:
        new_element = rules[f'{pair[0]}{pair[1]}']
        new_counter[(pair[0],new_element)] = new_counter.get((pair[0],new_element),0) + counter
        new_counter[(new_element,pair[1])] = new_counter.get((new_element,pair[1]),0) + counter
    return new_counter

def calculate_minmax(elements):
    min_element = min(elements.items(),key=lambda x: x[1])[1]
    max_element = max(elements.items(),key=lambda x: x[1])[1]
    return max_element - min_element

def calculate_polymer(data,steps):
    count_polymers = {(data['template'][i],data['template'][i+1]):1 for i in range(len(data['template'])-1)}
    last_element = data['template'][-1]
    count_elements = {}
    for _ in range(steps):
        count_polymers = create_polymer_optimized(data['rules'],count_polymers)
    for element,value in count_polymers.items():
        count_elements.setdefault(element[0],0)
        count_elements[element[0]] += value
    count_elements[last_element] += 1
    return calculate_minmax(count_elements)

def part_one(data,steps=10):
    return calculate_polymer(data,steps)
     

def part_two(data,steps=40):
    return calculate_polymer(data,steps)

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
        