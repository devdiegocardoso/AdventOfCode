import pathlib
import sys
from dataclasses import dataclass, field
from heapq import heappush, heappop
def parse(puzzle_input):
    list_tmp = [line for line in puzzle_input.split('\n')]
    return [[int(item) for item in line ] for line in list_tmp]

@dataclass(order=True)
class Cell:
    x: int = field(compare=False)
    y: int = field(compare=False)
    cost: int


possible_moves = [(0,1),(0,-1),(1,0),(-1,0)]

def is_safe_move(point,limits):
    return (
        point[0] >= limits['inf_l'] and point[0] < limits['sup_l']
        and
        point[1] >= limits['inf_c'] and point[1] < limits['sup_c']
    )

def minimun_cost(costs,start,end,limits):
    acc_cost = [[9999 for _ in range(len(costs[0]))] for _ in range(len(costs))]
    visited = [[False for _ in range(len(costs[0]))] for _ in range(len(costs))]

    q = []
    acc_cost[start[0]][start[1]] = costs[start[0]][start[1]]
    heappush(q,Cell(start[0],start[1],costs[start[0]][start[1]]))

    while q:
        cell = heappop(q)
        x,y = cell.x, cell.y

        if visited[x][y]:
            continue

        visited[x][y] = True
        for point in possible_moves:
            next_line = point[0] + x
            next_column = point[1] + y
            if is_safe_move((next_line,next_column),limits) and not visited[next_line][next_column]:
                acc_cost[next_line][next_column] = min(
                    acc_cost[next_line][next_column],
                    acc_cost[x][y] + costs[next_line][next_column]
                    )
                heappush(q,Cell(next_line,next_column,acc_cost[next_line][next_column]))

    return acc_cost[end[0]][end[1]]-costs[start[0]][start[1]]


def part_one(costs):
    limits = {'inf_l':0,'inf_c':0,'sup_l':len(costs),'sup_c':len(costs[0])}
    return minimun_cost(costs,(0,0),(len(costs)-1,len(costs[0])-1),limits)
    
def expand_costs(costs,limits):
    expand_line = limits['sup_l']
    expand_column = limits['sup_c']
    expand_time = 5

    new_costs = [[0 for _ in range(expand_column*expand_time)] for _ in range(expand_line*expand_time)]

    for line in range(expand_line*expand_time):
        for column in range(expand_column):
            last_value = costs[line][column] if line < expand_line else new_costs[line][column]
            new_costs[line][column] = last_value
            for expansion in range(1,expand_time):
                last_value += 1
                if last_value > 9:
                    last_value = 1
                if line < expand_line:
                    new_costs[expand_line*expansion+line][column] = last_value
                new_costs[line][expand_column*expansion+column] = last_value
    return new_costs

def part_two(costs):
    limits = {'inf_l':0,'inf_c':0,'sup_l':len(costs),'sup_c':len(costs[0])}
    new_costs = expand_costs(costs,limits)
    limits = {'inf_l':0,'inf_c':0,'sup_l':len(new_costs),'sup_c':len(new_costs[0])}

    #print(new_costs[0])
    return minimun_cost(new_costs,(0,0),(len(new_costs)-1,len(new_costs[0])-1),limits)

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
        