import pathlib
import sys
from functools import reduce
def parse(puzzle_input):
    return [[int(element) for element in line]for line in puzzle_input.split('\n')]

def parse_list(puzzle_input):
    list_tmp = [line for line in puzzle_input.split()]
    return [(list_tmp[i], int(list_tmp[i+1])) for i in range(0,len(list_tmp),2)]

def find_highpoints(matrix,element,adjacent_points):
    points_greater_than_element = sum(
        matrix[point[0]][point[1]] > element
        for point in adjacent_points
    )

    return points_greater_than_element == len(adjacent_points)

def verify_heightmap(matrix,x,y,limits):
    pairs = []
    if x != limits['inferior_x']:
        pairs.append((x-1,y))
    if x != limits['superior_x']:
        pairs.append((x+1,y))
    if y != limits['inferior_y']:
        pairs.append((x,y-1))
    if y != limits['superior_y']:
        pairs.append((x,y+1))
    return find_highpoints(matrix,matrix[x][y],pairs)

def part_one(numbers):
    lower_points = []
    lower_points_coordinates = []
    limits = {
        'inferior_x': 0, 'inferior_y': 0,
        'superior_x':len(numbers)-1,"superior_y":len(numbers[0])-1
        }
    
    for x in range(len(numbers)):
        for y in range(len(numbers[x])):
            if verify_heightmap(numbers,x,y,limits):
                lower_points.append(numbers[x][y]+1)
                lower_points_coordinates.append((x,y))

    return sum(lower_points),lower_points_coordinates,limits

def is_not_queued(visited,queue,coord):
    return coord not in visited and coord not in queue

def verify_boundary(coord,limit,type=1):
    return coord+1 <= limit if type == 1 else coord-1 >= limit
        
def verify_max_height(value,limit=9):
    return value != limit

def traverse_points(matrix,x,y,limits,visited,queue):
    if verify_boundary(x,limits['superior_x']) and verify_max_height(matrix[x+1][y]) and is_not_queued(visited,queue,(x+1,y)):
        queue.append((x+1,y))
    if verify_boundary(x,limits['inferior_x'],0) and verify_max_height(matrix[x-1][y])  and is_not_queued(visited,queue,(x-1,y)):
        queue.append((x-1,y))
    if verify_boundary(y,limits['superior_y']) and verify_max_height(matrix[x][y+1]) and is_not_queued(visited,queue,(x,y+1)):
        queue.append((x,y+1))
    if verify_boundary(y,limits['inferior_y'],0) and verify_max_height(matrix[x][y-1])  and is_not_queued(visited,queue,(x,y-1)):
        queue.append((x,y-1))

def count_basin_region(matrix,coordinate,limits):
    visited_coordinates = []
    queue = [coordinate]
    while queue:
        current = queue.pop(0)
        visited_coordinates.append(current)
        x,y = current
        traverse_points(matrix,x,y,limits,visited_coordinates,queue)
    
    return len(visited_coordinates)

    

def part_two(numbers,lower_points_coordinates,limits):
    basin_sizes = []
    for coordinate in lower_points_coordinates:
        size = count_basin_region(numbers,coordinate,limits)
        basin_sizes.append(size)
    return reduce(lambda x,y: x*y,sorted(basin_sizes)[-3:])

def solve(puzzle_input):
    numbers = parse(puzzle_input)
    solution_1,lower_points_coordinates, limits = part_one(numbers)
    solution_2 = part_two(numbers,lower_points_coordinates,limits)

    return solution_1,solution_2

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str,solutions)))
        