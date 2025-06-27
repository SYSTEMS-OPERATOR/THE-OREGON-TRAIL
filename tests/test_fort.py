import builtins
from or78_vars import GameGlobals
from or78_3_loop import fort


def test_fort_adds_correct_supplies(monkeypatch):
    g = GameGlobals()
    g.cash_total = 100
    g.amount_spent_on_food = 0
    g.amount_spent_on_bullets = 0
    g.amount_spent_on_clothing = 0
    g.amount_spent_on_miscellaneous = 0

    inputs = iter(["30", "0", "0", "0"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    fort(g)

    assert g.cash_total == 70
    assert g.amount_spent_on_food == 20
    assert g.amount_spent_on_bullets == 0
    assert g.amount_spent_on_clothing == 0
    assert g.amount_spent_on_miscellaneous == 0
