import pathlib
import sys
from copy import deepcopy


def parse_list(puzzle_input):
    list_tmp = [line for line in puzzle_input.split('\n')]
    return [[int(item) for item in line] for line in list_tmp]

def increase_energy_by_octopus(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
             matrix[i][j] += 1

def get_matrix_limits(matrix):
    return {'inf_c': 0, 'inf_l': 0, 'sup_c': len(matrix[0]), 'sup_l': len(matrix)}

def remove_from_list(tuple,limits):
    return (
        tuple[0] < limits['inf_l']
        or tuple[1] < limits['inf_c']
        or tuple[0] >= limits['sup_l']
        or tuple[1] >= limits['sup_c']
    )

def generate_matrix_coordinates(i,j,limits):
    points = [
        (i-1,j-1),(i-1,j),(i-1,j+1),
        (i,j-1),(i,j+1),
        (i+1,j-1),(i+1,j),(i+1,j+1)
        ]
    return [pair for pair in points if not remove_from_list(pair,limits)]


def propagate_flash(matrix,limits,flashed):
    points = [(k,l) for i,j in flashed for k,l in generate_matrix_coordinates(i,j,limits)]

    while points:
        l, c = points.pop(0)
        matrix[l][c] += 1
        if matrix[l][c] > 9 and (l,c) not in flashed:
            flashed.append((l,c))
            points.extend(generate_matrix_coordinates(l,c,limits))

    return len(flashed)


def spend_accumulated_energy(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 9:
                matrix[i][j] = 0 

def flash(matrix,limits):
    lines = len(matrix)
    columns = len(matrix[0])
    flashed = [(i,j) for i in range(lines) for j in range(columns) if matrix[i][j] > 9]
    flashes = propagate_flash(matrix,limits,flashed)
    spend_accumulated_energy(matrix)
    return flashes

def print_matrix(matrix):
    for line in matrix:
        print(line)
    print()

def part_one(numbers,steps=100):
    matrix = deepcopy(numbers)
    limits = get_matrix_limits(matrix)
    total_flashes = 0
    for _ in range(steps):
        increase_energy_by_octopus(matrix)
        total_flashes += flash(matrix,limits)
    return total_flashes

def are_octopuses_synchronized(matrix):
    return all(item == 0 for line in matrix for item in line)

def part_two(numbers):
    matrix = deepcopy(numbers)
    limits = get_matrix_limits(matrix)
    turn = 0
    while not are_octopuses_synchronized(matrix):
        increase_energy_by_octopus(matrix)
        flash(matrix,limits)
        turn += 1
    return turn

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
        