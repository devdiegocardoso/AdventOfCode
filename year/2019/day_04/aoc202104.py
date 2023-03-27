import pathlib
import sys

def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split()]

def create_dict(p_list):
    return {
        'drawn_numbers': [int(x) for x in p_list[0].split(',')],
        'boards': {},
        'winners': []
    }

def fill_dict(board, item, dict_bingo):
    if board not in dict_bingo['boards']:
        dict_bingo['boards'][board] = {}
    dict_bingo['boards'][board].update({int(item): False})

def parse_list(puzzle_input):
    list_tmp = [line for line in puzzle_input.split()]
    dict_bingo = create_dict(list_tmp)

    list_tmp.pop(0)
    board = 1
    for board_validate, item in enumerate(list_tmp, start=1):
        fill_dict(board,item, dict_bingo)
        if board_validate % 25 == 0:
            board += 1
    return dict_bingo

def is_number_marked(board,numbers,position):
    return board[numbers[position]]

def count_board_columns(board,numbers,line):
    return sum(
        1
        for _ in filter(
            lambda column: is_number_marked(
                board, numbers, line + (column * 5)
            ),
            range(5),
        )
    )
def count_board_lines(board,numbers,line):
    return sum(
        1
        for _ in filter(
            lambda column: is_number_marked(
                board, numbers, (line * 5) + column
            ),
            range(5),
        )
    )

def count_board(board,numbers,line, mode):
    return count_board_lines(board,numbers,line) if mode == 'line' else count_board_columns(board,numbers,line)

def scan(board , mode):
    list_numbers = extract_list_numbers(board)
    for line in range(5):
        total = count_board(board, list_numbers, line, mode)
        if total == 5:
            return True
    return False

def extract_list_numbers(board):
    return [n for n in board]

def find_board_winners(boards, winners):
    for board in boards:
        if board not in winners and (
            scan(boards[board], 'line')
            or not scan(boards[board], 'line')
            and scan(boards[board], 'column')
        ):
            winners.append(board)


def solve_winner(board, last_number):
    total = sum(number for number in board if not board[number])
    return total * last_number


def restart_boards(boards):
    for board in boards:
        for number in boards[board]:
            boards[board][number] = False

def mark_board(bingo,number):
    for board in bingo['boards']:
        if number in bingo['boards'][board]:
            bingo['boards'][board][number] = True

def find_winners(bingo,rounds):
    if rounds >= 5:
        find_board_winners(bingo['boards'], bingo['winners'])
    return len(bingo['winners'])

def solve_first(bingo,verified_boards, number):
    return solve_winner(bingo['boards'][bingo['winners'][0]], number) if verified_boards > 0 else -1

def solve_last(bingo,verified_boards, total_boards, number):
    return solve_winner(bingo['boards'][bingo['winners'][-1]], number) if verified_boards == total_boards else -1

def solve_game(bingo,verified_boards,mode,number):
    total_boards = len(bingo['boards'])
    return solve_first(bingo,verified_boards, number) if mode == 'first' else solve_last(bingo,verified_boards, total_boards, number)

def play(bingo, mode):
    for rounds, number in enumerate(bingo['drawn_numbers'], start=1):
        mark_board(bingo,number)
        verified_boards = find_winners(bingo,rounds)
        solved = solve_game(bingo,verified_boards,mode,number)
        if solved != -1:
            return solved
    return -1


def part_one(bingo):
    return play(bingo, 'first')


def part_two(bingo):
    return play(bingo, 'last')


def solve(puzzle_input):
    bingo = parse_list(puzzle_input)
    solution_1 = part_one(bingo)
    restart_boards(bingo['boards'])
    solution_2 = part_two(bingo)

    return solution_1, solution_2


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str, solutions)))
