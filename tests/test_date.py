import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from or78_2_date import print_final_date

def test_print_final_date_august_first():
    assert print_final_date(125) == "FRIDAY AUGUST 1 1847"
