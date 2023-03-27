import pathlib
import sys


def parse_list(puzzle_input):
    list_tmp = [line for line in puzzle_input.split('\n')]
    points_end = False
    dict_data = {'points':[],'folds':[]}
    for item in list_tmp:
        if item == '':
            points_end = True
        elif not points_end:
            pair = [tmp for tmp in item.split(',')]
            dict_data['points'].append((int(pair[0]),int(pair[1])))
        else:
            dict_data['folds'].append(item)
        
    return dict_data

def print_m(points):
    max_line = max(points,key=lambda x: x[1])[1]
    max_column = max(points,key=lambda x: x[0])[0]
    m = ['.']*(max_line+1)
    for i in range(len(m)):
        m[i] = ['.'] * (max_column+1)
    for point in points:
        m[point[1]][point[0]] = '#'

    for line in m:
        for item in line:
            print('\u2588' if item == '#' else ' ',end='')
        print()
def fold_y(dictionary,matrix,max_l,max_c):
    folds = 0
    for item in dictionary['folds']:
        if 'y' in item:
            _,folds = item.split('=')
            folds = int(folds)

    for shift, line in enumerate(range(folds+1,max_l), start=2):
        for column in range(max_c):
            if matrix[line][column] == '#':
                matrix[(folds+1)-shift][column] = matrix[line][column]

def fold_line(points:set,fold):
    points_above_fold = {point for point in points if point[1] > fold}
    for point in points_above_fold:
        points.add((point[0],(fold-((point[1]%(fold+1))+1))))
        points.remove(point)

def fold_column(points:set,fold):
    points_above_fold = {point for point in points if point[0] > fold}
    for point in points_above_fold:
        points.add(((fold-((point[0]%(fold+1))+1)),point[1]))
        points.remove(point)

def fold_paper(points:set,list_folds_x,list_folds_y):
    for fold in list_folds_x:
        fold_column(points,fold)
    for fold in list_folds_y:
        fold_line(points,fold)

def part_one(dictionary):
    set_points = set(dictionary['points'])

    list_folds_x = [int(item.split('=')[1]) for item in dictionary['folds'] if 'x' in item]

    fold_column(set_points,list_folds_x.pop(0))
    
    return len(set_points)

def part_two(dictionary):
    set_points = set(dictionary['points'])
    list_folds_x = [int(item.split('=')[1]) for item in dictionary['folds'] if 'x' in item]
    list_folds_y = [int(item.split('=')[1]) for item in dictionary['folds'] if 'y' in item]
    fold_paper(set_points,list_folds_x,list_folds_y)

    print_m(set_points)
    return len(set_points)

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
        