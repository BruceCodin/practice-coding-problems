"""
Python code solves advent-code-2021: Day 6: Lanternfish (Part 1)
https://adventofcode.com/2021/day/6
"""

def read_input(filename: str) -> list[str]:
    """Read input txt file and return list of str inputs."""
    with open(filename, 'r', encoding="utf-8") as f:
        return f.readlines()

def parse_lines(input_lines: list[str]) -> list[str]:
    """Parse list of lines each line, strip and clean each line."""
    return [line.strip() for line in input_lines]

def conv_str_int(parse_lines: list[str]) -> list[int]:
    """Convert the list of strings to a list of int"""
    pass 

def simulate_days(int_lines: list[int] ,days: int) -> list[int]:
    """Simulate latern fish days"""
    pass 


def count_fish(days_lines: list[int]) -> int:
    """Get total number of latern fishes after simulated days"""
    pass 

if __name__ == "__main__":
    pass