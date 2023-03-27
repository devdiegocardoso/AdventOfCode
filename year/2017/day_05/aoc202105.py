import pathlib
import sys

def parse(puzzle_input):
    entries = [(pair[0].strip().split(','),pair[1].strip().split(',')) for pair in [coordinates.split('->') for coordinates in [line for line in puzzle_input.split('\n')]]]
    dict_coordinates = {}
    for i in range(len(entries)):
        x,y = entries[i]
        dict_coordinates[i] = {}
        dict_coordinates[i].update({'x1': int(x[0]), 'y1': int(x[1])})
        dict_coordinates[i].update({'x2': int(y[0]), 'y2': int(y[1])})
    return dict_coordinates

def parse_list(puzzle_input):
    list_tmp = [line for line in puzzle_input.split()]
    return [(list_tmp[i], int(list_tmp[i+1])) for i in range(0,len(list_tmp),2)]


def generate_matrix(matrix,points,diagonal=False):
    if points['x1'] == points['x2']:
        start, finish = points['y1'], points['y2']
        if start >= finish:
            start, finish = finish, start
        for i in range(start,finish+1):
            x,y = points['x1'],i
            matrix.setdefault((x,y), 0)
            matrix[(x,y)] += 1
    elif points['y1'] == points['y2']:
        start, finish = points['x1'], points['x2']
        if start >= finish:
            start, finish = finish, start
        for i in range(start,finish+1):
            x,y = i,points['y1']
            matrix.setdefault((x,y), 0)
            matrix[(x,y)] += 1
    elif (points['x1'] + points['y1'] != points['x2'] + points['y2']) and diagonal:
        x, y = (points['x2'], points['y2']) if points['x1'] > points['x2'] else (points['x1'], points['y1'])
        controller = abs(points['x1'] - points['x2'])
        i = 0
        while i <= controller:
            matrix.setdefault((x+i,y+i), 0)
            matrix[(x+i,y+i)] += 1
            i += 1
    elif (points['x1'] + points['y1'] == points['x2'] + points['y2']) and diagonal:
        x, y = (points['x1'], points['y1']) if points['x1'] < points['x2'] else (points['x2'], points['y2'])
        controller = abs(points['x1'] - points['x2'])
        i = 0
        while i <= controller:
            matrix.setdefault((x+i,y-i), 0)
            matrix[(x+i,y-i)] += 1
            i += 1

def evaluate_matrix(matrix):
    return sum(matrix[key] >= 2 for key in matrix)
    
def print_log(matrix):
    for line in matrix:
        for item in line:
            print(item if item > 0 else '.',end='')
        print()

def part_one(numbers):
    m = {}
    for point in numbers:
        generate_matrix(m, numbers[point])

    return evaluate_matrix(m)

def part_two(numbers):
    m = {}
    for point in numbers:
        generate_matrix(m, numbers[point],diagonal=True)

    return evaluate_matrix(m)

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
        