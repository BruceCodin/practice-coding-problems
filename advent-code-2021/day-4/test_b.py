""" pytest test file for day-3: a """
#pylint: skip-file

from b import parse_lines, bingo_draws, define_boards, final_score, play_game, has_bingo
import pytest 

class TestParseLines:
    @pytest.mark.parametrize(
    "line, expected",
    [   
        (["101\n", " 111 ", " 100\n"], ["101", "111", "100"]), 
    ])

    def test_parse_lines(self, line, expected):
        assert parse_lines(line) == expected 

class TestBingoDraws:
    def test_bingo_draws_basic(self):
        lines = [
            "7,4,9,5,11\n",
            "22 13 17 11  0",
            " 8  2 23  4 24",
        ]
        parsed = parse_lines(lines)
        assert bingo_draws(parsed) == ["7", "4", "9", "5", "11"]

class TestDefineBoards:
    def test_define_boards_two_boards(self):
        lines = [
            "1,2,3",
            "",
            "1 2",
            "3 4",
            "",
            "5 6",
            "7 8",
        ]
        parsed = parse_lines(lines)
        boards = define_boards(parsed)

        assert list(boards.keys()) == [1, 2]
        assert boards[1] == [["1", "2"], ["3", "4"]]
        assert boards[2] == [["5", "6"], ["7", "8"]]

def test_has_bingo_row():
    drawn = {"1", "2", "3"}
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]
    assert has_bingo(board, drawn) is True

class TestPlayGameExample:
    def test_example_last_winner_score(self):
        lines = [
            "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
            "",
            "22 13 17 11  0",
            " 8  2 23  4 24",
            "21  9 14 16  7",
            " 6 10  3 18  5",
            " 1 12 20 15 19",
            "",
            " 3 15  0  2 22",
            " 9 18 13 17  5",
            "19  8  7 25 23",
            "20 11 10 24  4",
            "14 21 16 12  6",
            "",
            "14 21 17 24  4",
            "10 16 15  9 19",
            "18  8 23 26 20",
            "22 11 13  6  5",
            " 2  0 12  3  7",
        ]

        # Expect the **last** winning board score, which is 1924
        assert play_game(lines) == 1924

class TestFinalScore:
    def test_final_score_simple(self):
        assert final_score("24", 188) == 4512

