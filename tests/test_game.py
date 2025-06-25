import builtins
import random
import or78
import or78_4_riders
import or78_5_events
import or78_6_mountain
from or78_vars import GameGlobals

class QuickGlobals(GameGlobals):
    def __init__(self):
        super().__init__()
        # shorten the journey so the test finishes quickly
        self.GOAL_IN_MILES = 50


def test_quick_game_run(monkeypatch, capsys):
    # predetermined responses for the game prompts
    inputs = iter([
        "n",   # instructions
        "3",   # shooting level
        "200", # oxen
        "100", # food
        "100", # ammunition
        "100", # clothing
        "100", # misc supplies
        "2",   # continue (choices)
        "2",   # eat moderately
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr(random, "random", lambda: 1.0)
    monkeypatch.setattr(random, "choice", lambda seq: seq[0])
    monkeypatch.setattr(or78_4_riders, "riders", lambda g: None)
    monkeypatch.setattr(or78_5_events, "events", lambda g: None)
    monkeypatch.setattr(or78_6_mountain, "mountain", lambda g: None)
    monkeypatch.setattr(or78, "GameGlobals", QuickGlobals)

    or78.game()
    output = capsys.readouterr().out
    assert "END" in output
