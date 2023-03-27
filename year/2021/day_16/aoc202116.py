import pathlib
import sys
from math import prod

def get_bits(hexadecimal):
    return format(int(hexadecimal,16),'04b')

def get_bits_vector(hexadecimal_sequence):
    return ''.join([get_bits(bits) for bits in hexadecimal_sequence])

def decode_number(bits):
    return int(bits,2)

operators = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1])
}

def decode(bits,versions):
    type_id, current_position = extract_header(bits,versions)
    numbers = []
    if type_id == 4:
        return extract_literal(current_position, bits)
    current_position = extract(current_position, bits, versions,numbers)
    result = operators[type_id](numbers)
    return current_position, result

def extract(current_position, bits, versions,numbers,bits_shift=1):
    if bits[current_position] == '0':
        return extract_by_length(current_position+bits_shift, bits, versions,numbers)
    return extract_by_packets(current_position+bits_shift,bits,versions,numbers)

def extract_header(bits,versions,version_bits = 3,type_bits=3):
    version = decode_number(bits[:version_bits])
    versions.append(version)
    shift = version_bits+type_bits
    return decode_number(bits[version_bits:shift]), shift

def extract_literal(current_position, bits, sequence_size=4,bits_shift=1):
    next_bits = True
    binary_sequence = ''
    while next_bits:
        next_bits = bits[current_position] == '1'
        binary_sequence += bits[
            current_position+bits_shift:current_position+bits_shift+sequence_size]
        current_position += sequence_size + bits_shift
    return current_position, decode_number(binary_sequence)

def extract_by_packets(current_position, bits, versions,numbers,shift_bits=11):
    total_packets = decode_number(bits[current_position:current_position+shift_bits])
    current_position += shift_bits
    for _ in range(total_packets):
        shifted_bits,number = decode(bits[current_position:],versions)
        numbers.append(number)
        current_position += shifted_bits
    return current_position

def extract_by_length(current_position, bits, versions,numbers,shift_bits=15):
    bits_length = decode_number(bits[current_position:current_position+shift_bits])
    current_position += shift_bits
    bits_length += current_position
    while current_position < bits_length:
        shifted_bits, number = decode(bits[current_position:],versions)
        numbers.append(number)
        current_position += shifted_bits
    return current_position

def part_one(hexadecimal_string):
    versions = []
    _, results = decode(get_bits_vector(hexadecimal_string),versions)
    return sum(versions), results

def solve(puzzle_input):
    solution_1, solution_2 = part_one(puzzle_input)

    return solution_1,solution_2

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str,solutions)))
        