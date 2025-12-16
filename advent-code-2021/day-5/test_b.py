"""pytest test file for day-5: a"""
# pylint: skip-file

import pytest
from b import (
    parse_lines,
    return_coordinates,
    check_ver_hor_dia,
    get_points,
    return_overlap_count,
)


class TestReturnCoordinates:
    @pytest.mark.parametrize(
        "lines, expected",
        [
            (["0,9 -> 5,9"], [["0", "9", "5", "9"]]),
            (["8,0 -> 0,8"], [["8", "0", "0", "8"]]),
            (
                ["1,1 -> 1,3", "9,7 -> 7,7"],
                [["1", "1", "1", "3"], ["9", "7", "7", "7"]],
            ),
        ],
    )
    def test_return_coordinates_basic(self, lines, expected):
        parsed = parse_lines(lines)
        assert return_coordinates(parsed) == expected


class TestCheckVerHorDia:
    @pytest.mark.parametrize(
        "coords, expected",
        [
            (["0", "9", "5", "9"], True),   # horizontal
            (["7", "0", "7", "4"], True),   # vertical
            (["2", "2", "2", "1"], True),   # vertical (reverse)
            (["9", "4", "3", "4"], True),   # horizontal (reverse)
            (["8", "0", "0", "8"], True),   # diagonal (45°)
            (["0", "0", "8", "8"], True),   # diagonal (45°)
        ],
    )
    def test_check_ver_hor_dia(self, coords, expected):
        assert check_ver_hor_dia(coords) is expected


class TestGetPoints:
    def test_get_points_single_horizontal(self):
        lines = ["0,9 -> 2,9"]
        parsed = parse_lines(lines)
        coords = return_coordinates(parsed)
        assert get_points(coords) == [(0, 9), (1, 9), (2, 9)]

    def test_get_points_single_vertical(self):
        lines = ["1,1 -> 1,3"]
        parsed = parse_lines(lines)
        coords = return_coordinates(parsed)
        assert get_points(coords) == [(1, 1), (1, 2), (1, 3)]

    def test_get_points_diagonal_45deg(self):
        lines = ["8,0 -> 0,8"]
        parsed = parse_lines(lines)
        coords = return_coordinates(parsed)
        assert get_points(coords) == [
            (8, 0), (7, 1), (6, 2), (5, 3), (4, 4),
            (3, 5), (2, 6), (1, 7), (0, 8),
        ]


class TestReturnOverlapCount:
    def test_overlap_count_aoc_example_part2(self):
        lines = [
            "0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2",
        ]
        parsed = parse_lines(lines)
        coords = return_coordinates(parsed)
        points = get_points(coords)
        assert return_overlap_count(points) == 12

