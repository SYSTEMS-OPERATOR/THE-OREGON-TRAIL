import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from or78_vars import GameGlobals
from or78_2_date import dates


def test_increment_turn_and_no_turns_left():
    g = GameGlobals()
    assert g.current_date == 0
    assert not g.no_turns_left(dates)
    g.increment_turn()
    assert g.current_date == 1
    assert not g.no_turns_left(dates)
    g.current_date = len(dates)
    assert g.no_turns_left(dates)
