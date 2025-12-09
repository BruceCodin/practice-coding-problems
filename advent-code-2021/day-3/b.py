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
    return [line.strip() for line in input_lines]

def most_common_bit(clean_lines: list[str], index: int,mode: str) -> str:
    """Return the most common bit at most left position (signficant bit)"""
    num_lines = len(clean_lines)

    count_1 = sum(line[index]=='1' for line in clean_lines)
    
    match mode:
        case 'co2': 
            if count_1 < num_lines/2:
                return '1' 
            else:
                return '0'
        case 'oxy': 
            return '1' if count_1 >= num_lines/2 else '0'

def get_oxygen_rating(input_lines: list[str]) -> int:
    """Filter and obtain the oxygen rating"""
    filtered_lines = parse_lines(input_lines)

    index = 0 
    line_len = len(filtered_lines[0])

    while index < line_len and len(filtered_lines) != 1:
        most_common = most_common_bit(filtered_lines, index, 'oxy')
        
        filtered_lines = [line for line in filtered_lines if line[index] == most_common]
        index += 1

    return int(filtered_lines[0],2)

def get_co2_scrubber_rating(input_lines: list[str]) -> int:
    """Filter and obtain the co2 scrubber rating"""
    filtered_lines = parse_lines(input_lines)

    index = 0 
    line_len = len(filtered_lines[0])

    while index < line_len and len(filtered_lines) != 1:
        most_common = most_common_bit(filtered_lines, index, 'co2')
        
        filtered_lines = [line for line in filtered_lines if line[index] == most_common]
        index += 1

    return int(filtered_lines[0],2)

def calculate_life_support(oxygen_rate: int, co2_scrubber_rate: int) -> int:
    """Caclculate the life support"""
    return oxygen_rate * co2_scrubber_rate

if __name__ == "__main__":
    line_inputs = read_input('input.txt')

    oxygen_rating = get_oxygen_rating(line_inputs)
    co2_rating = get_co2_scrubber_rating(line_inputs)

    print (calculate_life_support(oxygen_rating, co2_rating))