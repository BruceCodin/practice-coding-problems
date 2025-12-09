""" pytest test file for day-3: a """
#pylint: skip-file

from a import parse_lines, most_common_bits, get_gamma_rate, get_eplison_rate, calculate_power
import pytest 

class TestParseLines:
    @pytest.mark.parametrize(
    "line, expected",
    [   
        (["101\n", " 111 ", " 100\n"], ["101", "111", "100"]), 
    ])

    def test_parse_lines(self, line, expected):
        assert parse_lines(line) == expected 

class TestMostCommonBits:
    @pytest.mark.parametrize(
    "lines, expected",
    [
        (["011", "010", "111"],[0,1,1]),     
        (["101", "111", "100"], [1,0,1]), 
    ],
    )
    def test_most_common_bit(self, lines, expected):
        assert most_common_bits(lines) == expected

class TestGetGammaRate:
    def test_get_gamma_rate(self):
        assert get_gamma_rate((1,0,1)) == 5

class TestGetEplisonRate:
    def test_get_eplison_rate(self):
        assert get_eplison_rate((1,0,1)) == 2

# Would normally also test the calculate power but it's so simple I've skipped it
