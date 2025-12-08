""" pytest test file for day-1: a """
#pylint: skip-file

from b import parse_command, get_horizontal_depth, calculate_product
import pytest 

class TestParseCommand:
    @pytest.mark.parametrize(
    "line, expected",
    [
        ("forward 5", ("forward", 5)),
        ("down 3", ("down", 3)),
        ("up 7", ("up", 7)),
    ])
    
    def test_parse_command_basic(self, line, expected):
        assert parse_command(line) == expected

class TestGetHorizontalDepth:
    @pytest.mark.parametrize(
    "lines, expected",
    [
        (["forward 5"], (5, 0)),
        (["forward 5","down 5","forward 8"], (13, 40)),
    ])

    def test_get_horizontal_depth(self, lines, expected):
        assert get_horizontal_depth(lines) == expected

class TestCalculateProduct: 
    @pytest.mark.parametrize(
    "inputs, expected",
    [
        ((4,5), (20)),
        ((4,3), (12)),
    ])

    def test_calculate_product(self, inputs, expected):
        assert calculate_product(inputs[0],inputs[1]) == expected