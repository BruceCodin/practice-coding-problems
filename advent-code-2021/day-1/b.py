"""
Python code solves advent-code-2021: day 1 sonor sweep (part 2)
https://adventofcode.com/2021/day/1
"""

def read_input(filename: str) -> list[str]:
    """ Read input txt file and return list of str inputs """
    with open(filename, 'r') as f:
        return f.readlines()

def convert_list_str(input_lines: list[str]) -> list[int]:
    """ Converts list of str to list of int """
    return [int(x) for x in input_lines]

def count_increment(sliding_windows: list[tuple]) -> int:
    """ Returns count of how many times each subsequent sliding window sum increased from previous """
    sum_windows = []
    for i in range(len(sliding_windows)):
        sum_windows.append(sum(sliding_windows[i]))
    
    result_increments = 0
    for i in range(1, len(sum_windows)):
        if sum_windows[i] > sum_windows[i-1]:
            result_increments += 1

    return result_increments


def sliding_measurement(input_lines: list[str]) -> int:
    """ Get three measurement sliding window sums and how many times they increase """
    measurement_lines = convert_list_str(input_lines)

    sliding_windows = list(zip(measurement_lines, measurement_lines[1:], measurement_lines[2:]))

    return count_increment(sliding_windows)

if __name__ == "__main__":
    get_input = read_input('input.txt')
    print(sliding_measurement(get_input))