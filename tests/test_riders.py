import builtins
from or78_vars import GameGlobals
from or78_4_riders import outcome


def test_outcome_massacred_when_no_bullets(capsys):
    g = GameGlobals()
    g.amount_spent_on_bullets = 0
    g.hostility_of_riders = True
    outcome(g)
    captured = capsys.readouterr().out
    assert "MASSACRED" in captured
    assert g.dead
