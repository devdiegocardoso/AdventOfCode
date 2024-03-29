import pathlib
import sys

def parse(puzzle_input):
    return [(line) for line in puzzle_input.split()]

def parse_list(puzzle_input):
    list_tmp = [line for line in puzzle_input.split()]
    return [(list_tmp[i], int(list_tmp[i+1])) for i in range(0,len(list_tmp),2)]

def part_one(numbers):
    list_items = []
    watcher = 0
    for number in numbers:
        while watcher < len(number):
            pair = []
            if number[watcher] == '[' and number[watcher+1] != '[':
                watcher += 1
                while number[watcher] != ']':
                    if number[watcher] != ',':
                        pair.append(number[watcher])
                    watcher += 1
                list_items.append(pair)
            watcher += 1
    return list_items



def part_two(numbers):
    return

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
        