""" pytest test file for day-1: a """
#pylint: skip-file

from a import count_increment
import pytest 

class TestCountIncrement:
    """Tests for count_increment()."""

    @pytest.mark.parametrize(
        "readings, expected",
        [
            ([], 0),                                # empty list
            (["100"], 0),                           # single value
            (["1", "2", "3", "4", "4"], 3),         # mixed, last equal
            (["3", "2", "1"], 0),                   # strictly decreasing
            (["5", "5", "5"], 0),                   # all equal
            (["1", "2"], 1),                        # simple increase
        ],
    )
    def test_count_increment_various(self, readings, expected):
        assert count_increment(readings) == expected