"""
Python code solves advent-code-2021: Day 6: Lanternfish (Part 1)
https://adventofcode.com/2021/day/6
"""

def read_input(filename: str) -> list[str]:
    """Read input txt file and return list of str inputs."""
    with open(filename, 'r', encoding="utf-8") as f:
        return f.readlines()

def parse_lines(input_lines: list[str]) -> list[list[str]]:
    """Parse list of lines each line, strip and clean each line."""
    return [line.strip().split(',') for line in input_lines]

def conv_str_int(parsed_lines: list[list[str]]) -> list[int]:
    """Convert the list of strings to a list of int"""
    return [int(fish_str) for fish_str in parsed_lines[0]]

def simulate_days(int_lines: list[int], days: int) -> list[int]:
    """Simulate latern fish days"""
    
    result = int_lines
    new_day = [] # Need this as a store else we'll iterate over a list that we're modifying at the same time
    new_fish_counter = 0

    for days_i in range(days):
        for lines_i in result:
            if lines_i == 0:
                new_day.append(6)
                new_fish_counter += 1
            
            else: 
                new_day.append(lines_i-1)
        
        
        for new_fish in range(new_fish_counter):
            new_day.append(8)
        
        new_fish_counter = 0
        result = new_day
        new_day = []

    return result


def count_fish(days_lines: list[int]) -> int:
    """Get total number of latern fishes after simulated days"""
    return len(days_lines)

if __name__ == "__main__":
    input_lines = read_input('input.txt')
    parsed_lines = parse_lines(input_lines)
    int_lines = conv_str_int(parsed_lines)

    latern_fishes = simulate_days(int_lines, 80)
    print(count_fish(latern_fishes))