import builtins
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import or78
from or78_vars import GameGlobals


def test_game_completes(monkeypatch, capsys):
    class DummyGlobals(GameGlobals):
        def __init__(self):
            super().__init__()
            self.cash_total = 0
            self.total_mileage = self.GOAL_IN_MILES

    monkeypatch.setattr(or78, "GameGlobals", DummyGlobals)
    monkeypatch.setattr(or78, "init", lambda g: None)

    # Patch out game functions that require user interaction or randomness
    monkeypatch.setattr(or78, "print_date", lambda *_: None)
    monkeypatch.setattr(or78, "begin", lambda *_: None)
    monkeypatch.setattr(or78, "choices", lambda *_: None)
    monkeypatch.setattr(or78, "toggle_fort_presence", lambda *_: None)
    monkeypatch.setattr(or78, "eating", lambda *_: None)
    monkeypatch.setattr(or78, "riders", lambda *_: None)
    monkeypatch.setattr(or78, "events", lambda *_: None)
    monkeypatch.setattr(or78, "mountain", lambda *_: None)
    monkeypatch.setattr(or78, "final_turn", lambda *_: None)
    monkeypatch.setattr(or78, "death", lambda *_: None)
    monkeypatch.setattr(builtins, "input", lambda *_: "n")

    or78.game()
    captured = capsys.readouterr().out
    assert "END" in captured
