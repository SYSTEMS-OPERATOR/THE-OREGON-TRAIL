"""Mountain pass events and obstacles."""

import random
import or78_helpers


def blizzard(this_vars):
    """Blizzard event during a mountain pass."""

    print("BLIZZARD IN MOUNTAIN PASS--TIME AND SUPPLIES LOST")
    this_vars.is_blizzard = True
    this_vars.amount_spent_on_food -= 25
    this_vars.amount_spent_on_miscellaneous -= 10
    this_vars.amount_spent_on_bullets -= 300
    this_vars.total_mileage = (
        this_vars.total_mileage - 30 - (40 * random.random())
    )
    if this_vars.amount_spent_on_clothing < 18 + (2 * random.random()):
        or78_helpers.illness(this_vars)


def blue_mountain(this_vars):
    """Check for blizzard when crossing the Blue Mountains."""

    if this_vars.total_mileage < 1700:
        return

    if this_vars.has_cleared_blue_mountains:
        return
    else:
        this_vars.has_cleared_blue_mountains = True
        if random.random() < 0.7:
            blizzard(this_vars)


def south_pass(this_vars):
    """Cross the South Pass and possibly face a blizzard."""

    if this_vars.has_cleared_south_pass:
        blue_mountain(this_vars)
    else:
        this_vars.has_cleared_south_pass = True
        if random.random() < 0.8:
            blizzard(this_vars)
        else:
            print("YOU MADE IT SAFELY THROUGH SOUTH PASS--NO SNOW")


def rugged_mountain(this_vars):
    """Navigate the rugged mountain terrain."""

    print("RUGGED MOUNTAINS")
    if random.random() > 0.1:
        if random.random() > 0.11:
            print("THE GOING GETS SLOW")
            # Original BASIC used "M=M-45-RND(-1)/.02" which subtracts
            # 45 miles plus up to ~50 additional random miles.
            this_vars.total_mileage -= 45 + (random.random() / 0.02)
            south_pass(this_vars)
        else:
            print("WAGON DAMAGED!—LOSE TIME AND SUPPLIES")
            this_vars.amount_spent_on_miscellaneous -= 5
            this_vars.amount_spent_on_bullets -= 200
            # BASIC line was "M=M-20-30*RND(-1)" meaning travel is reduced by
            # 20 miles plus up to 30 additional random miles.
            this_vars.total_mileage -= 20 + (30 * random.random())
            south_pass(this_vars)
    else:
        print("YOU GOT LOST---LOSE VALUABLE TIME TRYING TO FIND TRAIL!")
        this_vars.total_mileage -= 60
        south_pass(this_vars)


def mountain(this_vars):
    """Main mountain handling routine."""

    if this_vars.total_mileage < this_vars.SOUTH_PASS_IN_MILES:
        return

    chance = random.random() * 10
    threshold = 9 - ((this_vars.total_mileage / 100 - 15) ** 2 + 72) / (
        (this_vars.total_mileage / 100 - 15) ** 2 + 12
    )
    if chance > threshold:
        south_pass(this_vars)
    else:
        rugged_mountain(this_vars)
