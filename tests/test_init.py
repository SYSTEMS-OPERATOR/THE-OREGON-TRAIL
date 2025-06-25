import builtins
import or78_1_intro as intro
from or78_vars import GameGlobals


def test_game_initialization(monkeypatch):
    inputs = iter([
        "n",  # no instructions
        "3",  # shooting level
        "200",  # oxen amount
        "100",  # food
        "100",  # ammunition
        "100",  # clothing
        "100",  # misc supplies
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    g = GameGlobals()
    intro.init(g)
    assert g.shooting_level == 3
    assert g.amount_spent_on_animals == 200
    assert g.amount_spent_on_food == 100
    assert g.amount_spent_on_bullets == 100
    assert g.amount_spent_on_clothing == 100
    assert g.amount_spent_on_miscellaneous == 100
    assert g.cash_total == 100

