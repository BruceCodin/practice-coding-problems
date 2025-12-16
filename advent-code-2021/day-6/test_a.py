"""pytest test file for day-6: a"""
# pylint: skip-file

import pytest

# test_day06.py
import pytest

from a import conv_str_int, simulate_days, count_fish


EXAMPLE_LINES = ["3,4,3,1,2\n"]


class TestConvStrInt:
    def test_converts_csv_line_to_ints(self):
        assert conv_str_int(EXAMPLE_LINES) == [3, 4, 3, 1, 2]

    def test_handles_trailing_newline_and_whitespace(self):
        assert conv_str_int([" 3,4,3,1,2  \n"]) == [3, 4, 3, 1, 2]


class TestSimulateDays:
    def test_simulates_1_day_example(self):
        # Initial: 3,4,3,1,2
        # After 1 day: 2,3,2,0,1
        assert simulate_days([3, 4, 3, 1, 2], days=1) == [2, 3, 2, 0, 1]

    def test_simulates_2_days_example(self):
        # After 2 days: 1,2,1,6,0,8
        assert simulate_days([3, 4, 3, 1, 2], days=2) == [1, 2, 1, 6, 0, 8]

    def test_simulates_18_days_example_count(self):
        final = simulate_days([3, 4, 3, 1, 2], days=18)
        assert len(final) == 26


class TestCountFish:
    def test_counts_list_length(self):
        assert count_fish([6, 8]) == 2

    def test_counts_after_simulation_example_18_days(self):
        final = simulate_days([3, 4, 3, 1, 2], days=18)
        assert count_fish(final) == 26
