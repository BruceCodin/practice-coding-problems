"""
Python code solves advent-code-2021: Day 2: Dive! (part 2)
https://adventofcode.com/2021/day/2
"""

def read_input(filename: str) -> list[str]:
    """Read input txt file and return list of str inputs"""
    with open(filename, 'r') as f:
        return f.readlines()
    
def parse_command(line:str) -> tuple[str,int]:
    """Parse each line and separate into direction and unit"""
    direction, value_str = line.split()
    return direction, int(value_str)

def get_horizontal_depth(readlines_input: list[str], aim: int = 0) -> tuple[int,int]:
    """Get the total horziontal and depth values"""
    horizontal = 0
    depth = 0

    for line in readlines_input:
        direction, units = parse_command(line)

        if direction == "forward":
            horizontal += units
            depth += units * aim
        else:
            aim += units if direction == "down" else -units

    return horizontal, depth

def calculate_product(horizontal:int, depth:int) -> int:
    """Calculate final product"""
    return horizontal * depth 

if __name__ == "__main__":
    file_input = read_input('input.txt')
    horizontal, depth = get_horizontal_depth(file_input)

    print(calculate_product(horizontal,depth))
    