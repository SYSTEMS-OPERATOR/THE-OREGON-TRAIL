import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import or78_helpers
from or78_vars import GameGlobals
from or78_6_mountain import mountain


def test_mountain_progress(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.5)
    monkeypatch.setattr(or78_helpers, "illness", lambda *args, **kwargs: None)
    g = GameGlobals()
    g.total_mileage = 1000
    mountain(g)
