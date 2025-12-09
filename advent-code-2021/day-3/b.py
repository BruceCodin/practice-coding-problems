"""
Python code solves advent-code-2021: Day 3: Binary Diagnostic (part 2)
https://adventofcode.com/2021/day/3
"""

def read_input(filename: str) -> list[str]:
    """Read input txt file and return list of str inputs."""
    with open(filename, 'r') as f:
        return f.readlines()

def parse_lines(input_lines: list[str]) -> list[str]:
    """Parse list of lines each line, strip and clean each line."""
    return [line.strip() for line in input_lines ]

def most_common_bit(clean_lines: list[str], target_bit: int) -> int:
    """Return the most common bit at most left position (signficant bit)"""
    num_lines = len(clean_lines)

    for line in clean_lines:
        count_1 = sum(line[0]=='1')
    
    match target_bit:
        case 0: 
            if count_1 > num_lines/2:
                return 1 
            else:
                return 0
        case 1: 
            1 if count_1 >= num_lines/2 else 0

def get_oxygen_rating() -> int:
    """Filter and obtain the oxygen rating"""
    pass 

def get_co2_scrubber_rating() -> int:
    """Filter and obtain the co2 scrubber rating"""
    pass 

def calculate_life_support(oxygen_rate: int, co2_scrubber_rate: int) -> int:
    """Caclculate the life support"""
    return oxygen_rate * co2_scrubber_rate

if __name__ == "__main__":
    pass