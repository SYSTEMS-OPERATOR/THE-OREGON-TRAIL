import builtins
import random
import or78
import or78_helpers
import or78_3_loop
import or78_4_riders
import or78_5_events
import or78_6_mountain
from or78_vars import GameGlobals


def test_full_game_completion(monkeypatch):
    """Run the main game loop with patched I/O and small goal."""

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

    class ShortGameGlobals(GameGlobals):
        def __init__(self):
            super().__init__()
            self.GOAL_IN_MILES = 50

    monkeypatch.setattr(or78, "GameGlobals", ShortGameGlobals)

    monkeypatch.setattr(or78_3_loop, "choices", lambda g: None)
    monkeypatch.setattr(or78, "choices", lambda g: None)
    monkeypatch.setattr(or78_3_loop, "eating", lambda g: setattr(g, "total_mileage", g.total_mileage + 60))
    monkeypatch.setattr(or78, "eating", lambda g: setattr(g, "total_mileage", g.total_mileage + 60))
    monkeypatch.setattr(or78_3_loop, "toggle_fort_presence", lambda g: None)
    monkeypatch.setattr(or78, "toggle_fort_presence", lambda g: None)
    monkeypatch.setattr(or78_helpers, "shooting", lambda *args, **kwargs: 0)
    monkeypatch.setattr(random, "random", lambda: 0)
    monkeypatch.setattr(or78_4_riders, "riders", lambda g: None)
    monkeypatch.setattr(or78, "riders", lambda g: None)
    monkeypatch.setattr(or78_5_events, "events", lambda g: None)
    monkeypatch.setattr(or78, "events", lambda g: None)
    monkeypatch.setattr(or78_6_mountain, "mountain", lambda g: None)
    monkeypatch.setattr(or78, "mountain", lambda g: None)

    or78.game()
