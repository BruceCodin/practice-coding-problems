""" pytest test file for day-3: b """
#pylint: skip-file

from b import parse_lines, most_common_bit, get_oxygen_rating, get_co2_scrubber_rating
import pytest 

class TestParseLines:
    @pytest.mark.parametrize(
        "lines, expected",
        [
            (["101\n", " 111 ", " 100\n"], ["101", "111", "100"]),
        ],
    )
    def test_parse_lines(self, lines, expected):
        assert parse_lines(lines) == expected


class TestMostCommonBit:
    @pytest.mark.parametrize(
        "lines, index, mode, expected",
        [
            # OXYGEN TESTS (most common, tie → '1')
            (["0", "1", "1"], 0, "oxy", "1"),   # more 1s
            (["0", "0", "1"], 0, "oxy", "0"),   # more 0s
            (["0", "1"], 0, "oxy", "1"),        # tie → '1'
            (["10", "11", "01"], 0, "oxy", "1"), # col0 => [1,1,0] → '1'
            (["10", "11", "01"], 1, "oxy", "1"), # col1 => [0,1,1] → '1'

            # CO2 TESTS (least common, tie → '0')
            (["0", "1", "1"], 0, "co2", "0"),   # least common is 0
            (["0", "0", "1"], 0, "co2", "1"),   # least common is 1
            (["0", "1"], 0, "co2", "0"),        # tie → '0'
            (["10", "11", "01"], 0, "co2", "0"), # col0 => [1,1,0] → least is 0
            (["10", "11", "01"], 1, "co2", "0"), # col1 => [0,1,1] → least is 0
        ],
    )
    def test_most_common_bit_basic(self, lines, index, mode, expected):
        assert most_common_bit(lines, index, mode) == expected


class TestRatingsExample:
    def test_get_oxygen_rating_example(self):
        lines = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        assert get_oxygen_rating(lines) == 23

    def test_get_co2_scrubber_rating_example(self):
        lines = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        assert get_co2_scrubber_rating(lines) == 10
