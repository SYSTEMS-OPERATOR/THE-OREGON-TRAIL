import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from or78_3_loop import spend


def test_spend_with_enough_money(capsys):
    purse, value, success = spend(5, 10)
    assert purse == 5
    assert value == 5
    assert success


def test_spend_not_enough_money(capsys):
    purse, value, success = spend(20, 10)
    captured = capsys.readouterr().out
    assert "YOU DON'T HAVE THAT MUCH" in captured
    assert purse == 10
    assert value == 20
    assert not success
