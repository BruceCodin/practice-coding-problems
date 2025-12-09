"""
Python code solves advent-code-2021: Day 3: Binary Diagnostic (part 1)
https://adventofcode.com/2021/day/3
"""

def read_input(filename: str) -> list[str]:
    """Read input txt file and return list of str inputs."""
    with open(filename, 'r') as f:
        return f.readlines()

def parse_lines(input_lines: list[str]) -> list[str]:
    """Parse list of lines each line, strip and clean each line."""
    return [line.strip() for line in input_lines ]

def most_common_bits(clean_lines: list[str]) -> list[int]:
    """Get most common bit in each position."""
    # total_lines = len(clean_lines)
    # line_length = len(clean_lines[0]) # Assume all lines have the same length  

    # result = []
    # for i in range(line_length):
    #     count_1 = sum (int(line[i]) for line in clean_lines)

    #     if count_1 >= total_lines/2:
    #         result.append(1)
    #     else:
    #         result.append(0)
    
    # return result
    num_lines = len(clean_lines)
    result: list[int] = []

    for column in zip(*clean_lines):
        count_1 = sum(bit == "1" for bit in column)
        result.append(1 if count_1 >= num_lines / 2 else 0)

    return result

def get_gamma_rate(common_bits: list[int]) -> int:
    """Get the gamma rate from common binary bits"""
    # gamma_rate_result = 0
    # binary_mult = 1

    # for bit in common_bits[::-1]:
    #     gamma_rate_result += bit * binary_mult

    #     binary_mult = binary_mult * 2
    
    # return gamma_rate_result

    binary_str = "".join(str(bit) for bit in common_bits)
    return int(binary_str, 2)

def get_eplison_rate(common_bits: list[int]) -> int:
    """Get the epsilon rate from least common binary bits"""
    # eplison_rate_result = 0
    # binary_mult = 1

    # for bit in common_bits[::-1]:
    #     eplison_rate_result += int(not(bit)) * binary_mult

    #     binary_mult = binary_mult * 2
    
    # return eplison_rate_result

    n_bits = len(common_bits)
    gamma = get_gamma_rate(common_bits)
    mask = (1 << n_bits) - 1 # Holy crap this is doing that left shift thing we did in FPGA
    return mask ^ gamma

def calculate_power(gamma_rate: int, eplison_rate: int) -> int:
    """Calculate the power consumption"""
    return gamma_rate * eplison_rate

if __name__ == "__main__":
    lines_input = read_input('input.txt')
    common_bits = most_common_bits(parse_lines(lines_input))

    gamma_rate = get_gamma_rate(common_bits)
    eplison_rate = get_eplison_rate(common_bits)

    print(calculate_power(gamma_rate, eplison_rate))