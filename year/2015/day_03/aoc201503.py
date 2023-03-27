import pathlib
import sys

def parse(puzzle_input):
    return puzzle_input

def get_current_house(point,direction):
    if direction == '>':
        return point[0], point[1] + 1
    elif direction == '<':
        return point[0], point[1] - 1
    elif direction == '^':
        return point[0] - 1, point[1]
    elif direction == 'v':
        return point[0] + 1, point[1]

def visit_houses(directions):
    houses_visited = {(0,0):1}
    last_visit = (0,0)
    for direction in directions:
        current_visit = get_current_house(last_visit,direction)
        houses_visited[current_visit] = houses_visited.get(current_visit,0)
        houses_visited[current_visit] += 1
        last_visit = current_visit
    return houses_visited

def visit_houses_with_robot(directions):
    houses_visited = {(0,0):1}
    last_visit_santa = (0,0)
    last_visit_robot = (0,0)
    for index,direction in enumerate(directions,1):
        last_visit = last_visit_robot if index % 2 == 0 else last_visit_santa
        current_visit = get_current_house(last_visit,direction)
        houses_visited[current_visit] = houses_visited.get(current_visit,0)
        houses_visited[current_visit] += 1
        if index % 2 == 0:
            last_visit_robot = current_visit
        else:
            last_visit_santa = current_visit
    return houses_visited

def count_repeated_houses(houses):
    return sum(1 for house in houses.values())

def part_one(numbers):
    houses = visit_houses(numbers)
    return count_repeated_houses(houses)

def part_two(numbers):
    houses = visit_houses_with_robot(numbers)
    return count_repeated_houses(houses)

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
        