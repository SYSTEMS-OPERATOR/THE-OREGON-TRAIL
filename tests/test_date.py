import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from or78_2_date import print_final_date


@pytest.mark.parametrize(
    "day_index,expected",
    [
        (124, "THURSDAY JULY 31 1847"),
        (125, "FRIDAY AUGUST 1 1847"),
        (155, "SUNDAY AUGUST 31 1847"),
        (156, "MONDAY SEPTEMBER 1 1847"),
        (216, "FRIDAY OCTOBER 31 1847"),
        (217, "SATURDAY NOVEMBER 1 1847"),
        (246, "SUNDAY NOVEMBER 30 1847"),
        (247, "MONDAY DECEMBER 1 1847"),
    ],
)
def test_print_final_date_boundaries(day_index, expected):
    assert print_final_date(day_index) == expected
