import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import or78_helpers
from or78_vars import GameGlobals
from or78_5_events import events_list, events as run_events


def test_all_events_execute(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.5)
    monkeypatch.setattr(or78_helpers, "shooting", lambda *args, **kwargs: 0)
    g = GameGlobals()
    for ev in events_list:
        g.dead = False
        ev(g)


def test_events_wrapper(monkeypatch):
    monkeypatch.setattr(random, "choice", lambda seq: seq[0])
    monkeypatch.setattr(random, "random", lambda: 0.5)
    monkeypatch.setattr(or78_helpers, "shooting", lambda *args, **kwargs: 0)
    g = GameGlobals()
    run_events(g)
