import builtins
import random

import or78
import or78_helpers
import or78_vars


def test_game_runs(monkeypatch):
    inputs = iter([
        "n",  # instructions
        "3",  # shooting level
        "200",  # oxen
        "100",  # food
        "100",  # ammo
        "100",  # clothing
        "100",  # misc
        "2",  # continue
        "1",  # eat poorly
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr(or78_helpers, "shooting", lambda *_, **__: 0)
    monkeypatch.setattr(random, "random", lambda: 0.5)
    monkeypatch.setattr(random, "choice", lambda seq: seq[0])

    original_init = or78_vars.GameGlobals.__init__

    def patched_init(self):
        original_init(self)
        self.GOAL_IN_MILES = 50

    monkeypatch.setattr(or78_vars.GameGlobals, "__init__", patched_init)

    or78.game()
