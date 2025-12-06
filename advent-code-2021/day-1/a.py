"""
Python code solves advent-code-2021: day 1 sonor sweep (part 1)
https://adventofcode.com/2021/day/1
"""

def read_input(filename: str) -> list[str]:
    """ Read input txt file and return list of str inputs """
    with open(filename, 'r') as f:
        return f.readlines()
    

def count_increment(list_input:list[str]) -> int: 
    """ Count how many times a depth measurement increases from the previous one. """
    if not list_input:
        return 0

    numbers = [int(x) for x in list_input]

    count_result = 0

    for i in range(1, len(list_input)):

        if numbers[i] > numbers[i-1]:
            count_result += 1
    
    return count_result


if __name__ == "__main__":
    pass 