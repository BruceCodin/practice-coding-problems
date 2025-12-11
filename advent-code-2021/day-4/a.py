"""
Python code solves advent-code-2021: Day 4: Giant Squid (part 1)
https://adventofcode.com/2021/day/4
"""

def read_input(filename: str) -> list[str]:
    """Read input txt file and return list of str inputs."""
    with open(filename, 'r') as f:
        return f.readlines()

def parse_lines(input_lines: list[str]) -> list[str]:
    """Parse list of lines each line, strip and clean each line."""
    return [line.strip() for line in input_lines]

def bingo_draws(parsed_lines: list[str]) -> list[str]:
    """Get the bingo numbers drawn"""
    return parsed_lines[0].split(',')

def define_boards(parsed_lines: list[str]) -> dict[int, list[list[str]]]:
    """Define the bingo boards from input.txt"""
    board_num = 1
    boards = {}
    current_board = []
    for board_lines in parsed_lines[2::]:
        if not board_lines: # if board_lines == ""
                boards[board_num] = current_board # Load current board into boards
                board_num += 1
                current_board = []
        else: 
            current_board.append(board_lines.split())

    if current_board: # Need this because the for loop ends before it stores the last current board (since input.txt doesn't end with a "")
         boards[board_num] = current_board

    return boards

def has_bingo(board: list[list[str]], drawn: set[str]) -> bool:
    """Return True if any row or column of the board is fully marked."""
    # check rows
    for row in board:
        if all(value in drawn for value in row):
            return True

    # check columns
    num_cols = len(board[0])
    for col in range(num_cols):
        if all(row[col] in drawn for row in board):
            return True

    # No bingo then return false
    return False

def unmarked_sum(bingo_draws: list[str], winning_board: set[str]):
    """Calculate the unmarked sum on bingo board"""
    total = 0 
    for row in winning_board:
            for value in row:
                if value not in bingo_draws:
                    total += int(value)
    return total

def final_score(final_draw: str, unmarked_sum: int) -> int:
    """Calculate final score"""
    return int(final_draw) * unmarked_sum

def play_game(input_lines: list[str]) -> int:
    """Play the bingo game"""
    parsed_lines = parse_lines(input_lines)

    draws = bingo_draws(parsed_lines)
    boards = define_boards(parsed_lines)

    drawn = set()
 
    for draw in draws:
        drawn.add(draw)

        for key, board in boards.items():
            is_bingo = has_bingo(board, drawn)

            if is_bingo:
                print(f'Board {key} has hit a bingo')
                unmark_sum = unmarked_sum(drawn, board)
                return final_score(draw, unmark_sum)
    
    raise RuntimeError("No winning board found")
    
if __name__ == "__main__":
    input_lines = read_input('input.txt')
    print(play_game(input_lines))