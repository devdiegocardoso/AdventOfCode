"""
[summary]
"""
import pathlib
import sys
from collections import Counter
def parse(puzzle_input):
    """[summary]

    Args:
        puzzle_input ([type]): [description]

    Returns:
        [type]: [description]
    """
    return [int(line) for line in puzzle_input.split(',')]

def parse_list(puzzle_input):
    """[summary]

    Args:
        puzzle_input ([type]): [description]

    Returns:
        [type]: [description]
    """
    list_tmp = [line for line in puzzle_input.split()]
    return [(list_tmp[i], int(list_tmp[i+1])) for i in range(0,len(list_tmp),2)]

def part_one(numbers):
    """[summary]

    Args:
        numbers ([type]): [description]
    """
    min_pos = min(numbers)
    max_pos = max(numbers)
    positions = Counter(numbers)
    min_fuels = [
        sum(abs(pos - i) * positions[pos] for pos in positions)
        for i in range(min_pos, max_pos + 1)
    ]

    return min(min_fuels)

def soma(N):
    vetor = [0]
    for cont in range(1,N+1):
        vetor.append(vetor[cont-1] + cont)
    return vetor

# def soma(N):
#     vetor = [0] * (N+1)
#     soma_rec(N,vetor)
#     return vetor


# def soma_rec(N,vetor):
#     if N == 0:
#         return 0
#     if vetor[N] != 0:
#         return vetor[N]
#     vetor[N] = N + soma_rec(N-1,vetor)
#     return vetor[N]

def part_two(numbers):
    """[summary]

    Args:
        numbers ([type]): [description]
    """
    min_pos = min(numbers)
    max_pos = max(numbers)
    somas = soma(max_pos-min_pos)
    positions = Counter(numbers)
    min_fuels = [
        sum((somas[abs(pos - i)] * positions[pos]) for pos in positions)
        for i in range(min_pos, max_pos + 1)
    ]

    return min(min_fuels)

def solve(puzzle_input):
    """[summary]

    Args:
        puzzle_input ([type]): [description]

    Returns:
        [type]: [description]
    """
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
        