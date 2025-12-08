"""
Python code solves advent-code-2021: Day 2: Dive! (part 1)
https://adventofcode.com/2021/day/2
"""

def read_input(filename: str) -> list[str]:
    """Read input txt file and return list of str inputs"""
    with open(filename, 'r') as f:
        return f.readlines()

def parse_command(line:str) -> tuple[str,int]:
    """Parse each line and separate into direction and unit"""
    # line_clean = line.strip().split(' ')
    # return (line_clean[0], int(line_clean[1]))

    direction, value_str = line.split()
    return direction, int(value_str)
    

def get_horizontal_depth(readlines_input: list[str]) -> tuple[int,int]:
    """Get the total horziontal and depth values"""
    # if not readlines_input:
    #     return (0,0)
    
    # get_horizontal = 0 
    # get_depth = 0
    # for line in readlines_input:
    #     clean_line = parse_command(line)

    #     if clean_line[0] == 'forward':
    #         get_horizontal += clean_line[1]
        
    #     if clean_line[0] == 'up':
    #         get_depth -= clean_line[1]
        
    #     if clean_line[0] == 'down':
    #         get_depth += clean_line[1]
    
    # return (get_horizontal, get_depth)

    horizontal = 0
    depth = 0

    for line in readlines_input:
        direction, units = parse_command(line)

        if direction == "forward":
            horizontal += units
        else:
            depth += units if direction == "down" else -units

    return horizontal, depth

def calculate_product(horizontal:int, depth:int) -> int:
    """Calculate final product"""
    return horizontal * depth 

if __name__ == "__main__":
    file_input = read_input('input.txt')
    horizontal_depth = get_horizontal_depth(file_input)

    print(calculate_product(horizontal_depth[0],horizontal_depth[1]))