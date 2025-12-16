"""
Python code solves advent-code-2021: Day 5: Hydrothermal Venture (Part 2)
https://adventofcode.com/2021/day/5
"""
# You can use a pythonic libary , from collections, this avoids needing to use a dict to count
# from collections import Counter
# counts = Counter(points)
# return sum(v > 1 for v in counts.values())

def read_input(filename: str) -> list[str]:
    """Read input txt file and return list of str inputs."""
    with open(filename, 'r', encoding="utf-8") as f:
        return f.readlines()

def parse_lines(input_lines: list[str]) -> list[str]:
    """Parse list of lines each line, strip and clean each line."""
    return [line.strip() for line in input_lines]

def return_coordinates(lines: list[str]) -> list[list[str]]:
    """Return list of coordinates from parsed lines
    '0,9 -> 5,9' into ['0', '9', '5', '9']"""
    return [line.replace(" -> ", ",").split(",") for line in lines]

def check_ver_hor_dia(cords: list[str]) -> bool:
    """Checks if coordinates are vertical, horizontal or diagonal"""
    x_diff = max(int(cords[0]),int(cords[2])) - min((int(cords[0]),int(cords[2])))
    y_diff = max(int(cords[1]),int(cords[3])) - min((int(cords[1]),int(cords[3])))

    if cords[0] == cords[2] or cords[1] == cords[3]:
        return True 
    elif x_diff == y_diff:
        return True
    return False

def conv_int(cords: list[list[str]]) -> list[list[int]]:
    """Return list of str to list of int"""
    return [[int(n) for n in segment] for segment in cords]

def get_points(cords: list[list[str]]) -> list[tuple[int, int]]:
    """Return list of coordinate points covered by the lines"""
    coords_int = conv_int(cords)
    points: list[tuple[int, int]] = []

    for x1, y1, x2, y2 in coords_int:
        x_diff = max(x1,x2) - min(x1,x2)
        y_diff = max(y1,y2) - min(y1,y2)

        if x1 == x2:  # vertical
            start = min(y1, y2)
            end = max(y1, y2)
            for y in range(start, end + 1):
                points.append((x1, y))

        elif y1 == y2:  # horizontal
            start = min(x1, x2)
            end = max(x1, x2)
            for x in range(start, end + 1):
                points.append((x, y1))

        elif x_diff == y_diff: # diagonal
             dx = x2 - x1
             dy = y2 - y1 
            
             step_x = 1 if dx > 0 else -1
             step_y = 1 if dy > 0 else -1

             steps = abs(dx)
             
             x, y = x1, y1
             for _ in range(0, steps+1):
                 points.append((x,y))
                 x += step_x
                 y += step_y

    return points

def return_overlap_count(all_cords: list[tuple[int, int]]) -> int:
    """Return the integer number of all the points that overlap twice"""
    overlap_dict = dict()

    for cord in all_cords: 
        if cord in overlap_dict:
            overlap_dict[cord] += 1
        
        else: 
            overlap_dict[cord] = 1
    
    result = 0
    for cord_key, val in overlap_dict.items():
        if val > 1:
            result += 1
    
    return result


def main() -> int:
    """Main code"""
    line_input = read_input("input.txt")
    parsed_lines = parse_lines(line_input)

    coords = return_coordinates(parsed_lines)  # list[list[str]]

    checked_coords = []
    for c in coords:
        if check_ver_hor_dia(c):
            checked_coords.append(c)

    points_all = get_points(checked_coords)
    return return_overlap_count(points_all)

if __name__ == "__main__":
    print(main())