import sys
import os
from unittest import mock
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from or78_vars import GameGlobals
from or78_6_mountain import blizzard


def test_blizzard_event_damages_and_flags():
    g = GameGlobals()
    g.total_mileage = 1000
    g.amount_spent_on_food = 100
    g.amount_spent_on_miscellaneous = 50
    g.amount_spent_on_bullets = 400
    g.amount_spent_on_clothing = 10

    with mock.patch('random.random', return_value=0):
        with mock.patch('or78_helpers.illness') as mock_illness:
            blizzard(g)
            mock_illness.assert_called_once_with(g)

    assert g.is_blizzard
    assert g.amount_spent_on_food == 75
    assert g.amount_spent_on_miscellaneous == 40
    assert g.amount_spent_on_bullets == 100
    assert g.total_mileage == 970
