import pathlib
import sys

def parse(puzzle_input):
    formatted = puzzle_input.replace('target area: ','')
    x,y = formatted.split(', ')
    x = x.replace('x=','')
    y = y.replace('y=','')
    x = x.split('..')
    y = y.split('..')
    return {
        'inf_x': int(x[0]),
        'sup_x': int(x[1]),
        'inf_y': int(y[0]),
        'sup_y': int(y[1]),
    }

def is_inside_target(point,limits):
    return (limits['inf_x'] <= point[0] <= limits['sup_x'] 
            and 
            limits['inf_y'] <= point[1] <= limits['sup_y'])

def is_outside_target(point,limits):
    return (point[0] > limits['sup_x'] 
            or 
            point[1] < limits['inf_y'])

def find_max_high(limits):
    max_y_inside = []
    points = []
    for x in range(limits['sup_x']+1):
        for y in range(limits['inf_y'],abs(limits['inf_y'])+1):
            current_x = x
            current_y = y
            current_position = (0,0)
            stop_search = False
            max_y = 0
            while not stop_search:
                current_position = (current_position[0]+current_x,current_position[1]+current_y)
                max_y = max(max_y,current_position[1])
                stop_search = is_inside_target(current_position,limits) or is_outside_target(current_position,limits)
                if current_x > 0:
                    current_x -= 1
                elif current_x < 0:
                     current_x += 1
                current_y -= 1
            if is_inside_target(current_position,limits):
                points.append((x,y))
                max_y_inside.append(max_y)
    return max(max_y_inside), len(points)

def part_one(limits):
    return find_max_high(limits)[0]

def part_two(limits):
    return find_max_high(limits)[1]

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
        