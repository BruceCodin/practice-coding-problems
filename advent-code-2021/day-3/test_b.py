""" pytest test file for day-3: b """
#pylint: skip-file

from b import parse_lines, most_common_bit, get_oxygen_rating, get_co2_scrubber_rating
import pytest 

class TestParseLines:
    @pytest.mark.parametrize(
    "line, expected",
    [   
        (["101\n", " 111 ", " 100\n"], ["101", "111", "100"]), 
    ])

    def test_parse_lines(self, line, expected):
        assert parse_lines(line) == expected 