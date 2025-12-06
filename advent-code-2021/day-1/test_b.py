""" pytest test file for day-1: b """
#pylint: skip-file

from b import convert_list_str, count_increment, sliding_measurement
import pytest 

class TestConvertListStr:
    """ Tests for convert_list_str """

    @pytest.mark.parametrize(
        "input_lines, expected",
        [
            ([], []),  # empty list
            (["1", "2", "3"], [1, 2, 3]),  # simple case
            (["10\n", " 20 ", "003"], [10, 20, 3]),  # whitespace / leading zeros
        ],
    )

    def test_convert_list_str_basic(self, input_lines, expected):
        assert convert_list_str(input_lines) == expected


class TestCountIncrement:
    """ Tests for count_increment """
    @pytest.mark.parametrize(
        "windows, expected",
        [
            ([], 0),  # no windows at all
            ([(1, 2, 3)], 0),  # single window -> no comparison
            ([(1, 2, 3), (2, 3, 4)], 1),  # [6, 9] -> 1 increase
            ([(3, 3, 3), (1, 1, 1)], 0),  # [9, 3] -> no increase
            ([(1, 1, 1), (1, 1, 1)], 0),  # [3, 3] -> equal, no increase
        ],
    )

    def test_count_increment_windows(self, windows, expected):
        assert count_increment(windows) == expected


class TestSlidingMeasurement:
    """ Tests for sliding_measurement """
    def test_sliding_measurement_small_example(self):
        # readings: 1, 2, 3, 4
        # windows: [1,2,3] = 6, [2,3,4] = 9 -> 1 increase
        readings = ["1", "2", "3", "4"]
        assert sliding_measurement(readings) == 1

    def test_sliding_measurement_aoc_example(self):
        readings = [
            "199", "200", "208", "210", "200",
            "207", "240", "269", "260", "263",
        ]
        # From the problem statement, expected result is 5
        assert sliding_measurement(readings) == 5