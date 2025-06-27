"""Helper functions for user input and random events."""

import random
import time


def input_yes_no(message):
    """Return ``True`` if the user's reply starts with ``y`` (case-insensitive)."""

    reply = input(message)
    return reply.strip().lower().startswith("y")


def input_int(message):
    """Prompt ``message`` until the user enters an integer."""

    text_2_int = None
    while text_2_int is None:
        try:
            text_2_int = int(input(message))
        except ValueError:
            text_2_int = None
    return text_2_int


def shooting(shooting_level):
    """Return the player's shooting response time."""

    words = ["bang", "blam", "pow", "wham"]
    word = random.choice(words)
    t0 = time.time()
    typed_word = input(f"TYPE {word}: ")
    t1 = time.time()
    response_time = (t1 - t0) - (shooting_level - 1)
    if typed_word != word:
        return 9
    return max(response_time, 0)


def illness(this_vars):
    """Simulate the outcome of an illness event."""

    RND = random.random()
    if 100 * RND < 10 + 35 * (this_vars.choice_of_eating - 1):
        print("MILD ILLNESS---MEDICINE USED")
        this_vars.total_mileage -= 5
        this_vars.amount_spent_on_miscellaneous -= 2
    elif 100 * RND < 100 - (40 / 4 ** (this_vars.choice_of_eating - 1)):
        print("BAD ILLNESS---MEDICINE USED")
        this_vars.total_mileage -= 5
        this_vars.amount_spent_on_miscellaneous -= 5
    else:
        print("SERIOUS ILLNESS")
        print("YOU MUST STOP FOR MEDICAL ATTENTION")
        this_vars.amount_spent_on_miscellaneous -= 10
        this_vars.has_illness = True
