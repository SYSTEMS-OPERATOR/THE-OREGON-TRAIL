"""Random events that can occur during the journey."""

import random
import or78_helpers


def cold_weather(this_vars):
    """Deal with cold weather and determine if the party survives."""

    enough_clothes = (
        this_vars.amount_spent_on_clothing > 22 + (4 * random.random())
    )
    c_message = "" if enough_clothes else "DON'T "
    message = (
        "COLD WEATHER---BRRRRRRR!---YOU {}HAVE ENOUGH CLOTHING "
        "TO KEEP YOU WARM".format(c_message)
    )
    print(message)
    if not enough_clothes:
        this_vars.is_sufficient_clothing = True
        this_vars.dead = True


def heavy_rains(this_vars):
    """Simulate heavy rains slowing progress and costing supplies."""

    print("HEAVY RAINS---TIME AND SUPPLIES LOST")
    this_vars.amount_spent_on_food -= 10
    this_vars.amount_spent_on_bullets -= 500
    this_vars.amount_spent_on_miscellaneous -= 15
    # BASIC: M=M-5-10*RND(-1)
    # Subtract at least five miles plus an additional 0..10
    # The previous implementation accidentally allowed mileage to
    # increase when ``random.random()`` returned a value under 0.5.
    this_vars.total_mileage -= 5 + (10 * random.random())


def got_shot(this_vars):
    """Handle an event where a traveler is shot."""

    print("YOU GOT SHOT IN THE LEG AND THEY TOOK ONE OF YOUR OXEN")
    print("BETTER HAVE A DOC LOOK AT YOUR WOUND")
    this_vars.is_injured = True
    this_vars.amount_spent_on_miscellaneous -= 5
    this_vars.amount_spent_on_animals -= 20


# events array
def weather(this_vars):
    """Trigger weather events depending on distance traveled."""

    if this_vars.total_mileage > this_vars.SOUTH_PASS_IN_MILES:
        cold_weather(this_vars)
    else:
        heavy_rains(this_vars)


def wagon_break_down(this_vars):
    """Handle wagon breakdown event."""

    print("WAGON BREAKS DOWN--LOSE TIME AND SUPPLIES FIXING IT")
    # BASIC: M=M-15-5*RND(-1) -> subtract 15 plus up to 5 extra miles
    this_vars.total_mileage -= 15 + (5 * random.random())
    this_vars.amount_spent_on_miscellaneous -= 8


def ox_injuries(this_vars):
    """Simulate an ox injury."""

    print("OX INJURES LEG--SLOWS YOU DOWN REST OF TRIP")
    this_vars.total_mileage -= 25
    this_vars.amount_spent_on_animals -= 20


def arm_broke(this_vars):
    """Event where a family member breaks an arm."""

    print("BAD LUCK--YOUR DAUGHTER BROKE HER ARM")
    print("YOU HAD TO STOP AND USE SUPPLIES TO MAKE A SLING")
    # BASIC: M=M-5-4*RND(-1)
    this_vars.total_mileage -= 5 + (4 * random.random())
    # BASIC: M1=M1-2-3*RND(-1)
    this_vars.amount_spent_on_miscellaneous -= 2 + (3 * random.random())


def ox_wander(this_vars):
    """An ox wanders off causing delay."""

    print("OX WANDERS OFF--SPEND TIME LOOKING FOR IT")
    this_vars.total_mileage -= 17


def helpful_indians(this_vars):
    """Friendly natives help find food."""

    # Typographical fix: "where" rather than "were".
    print("HELPFUL INDIANS SHOW YOU WHERE TO FIND MORE FOOD")
    this_vars.amount_spent_on_food += 14


def lost_son(this_vars):
    """Child lost event costing time."""

    print("YOUR SON GETS LOST---SPEND HALF THE DAY LOOKING FOR HIM")
    this_vars.total_mileage -= 10


def unsafe_water(this_vars):
    """Unsafe water delays the party."""

    print("UNSAFE WATER--LOSE TIME LOOKING FOR CLEAN SPRING")
    # BASIC: M=M-10*RND(-1)-2 -> subtract 2 plus up to 10 more miles
    this_vars.total_mileage -= 2 + (10 * random.random())


def wagon_fire(this_vars):
    """Handle damage from a wagon fire."""

    print("THERE WAS A FIRE IN YOUR WAGON--FOOD AND SUPPLIES DAMAGE!")
    this_vars.amount_spent_on_food -= 40
    this_vars.amount_spent_on_bullets -= 400
    # BASIC: M1=M1-RND(-1)*8-3
    this_vars.amount_spent_on_miscellaneous -= 3 + (8 * random.random())
    this_vars.total_mileage -= 15


def heavy_fog(this_vars):
    """Heavy fog event slowing down travel."""

    print("LOSE YOUR WAY IN HEAVY FOG---TIME IS LOST")
    # BASIC: M=M-10-5*RND(-1)
    this_vars.total_mileage -= 10 + (5 * random.random())


def snake_poison(this_vars):
    """Snake bite event possibly lethal."""

    print("YOU KILLED A POISONOUS SNAKE AFTER IT BIT YOU")
    this_vars.amount_spent_on_bullets -= 10
    this_vars.amount_spent_on_miscellaneous -= 5
    if this_vars.amount_spent_on_miscellaneous < 0:
        print("YOU DIE OF SNAKEBITE SINCE YOU HAVE NO MEDICINE")
        this_vars.dead = True


def wagon_swamped(this_vars):
    """Wagon gets swamped while fording a river."""

    print("WAGON GETS SWAMPED FORDING RIVER--LOSE FOOD AND CLOTHES")
    this_vars.amount_spent_on_food -= 30
    this_vars.amount_spent_on_clothing -= 20
    # BASIC: M=M-20-20*RND(-1)
    this_vars.total_mileage -= 20 + (20 * random.random())


def hail_storm(this_vars):
    """Hail storm damages supplies."""

    print("HAIL STORM---SUPPLIES DAMAGED")
    # BASIC: M=M-5-RND(-1)*10
    this_vars.total_mileage -= 5 + (10 * random.random())
    this_vars.amount_spent_on_bullets -= 200
    # BASIC: M1=M1-4-RND(-1)*3
    this_vars.amount_spent_on_miscellaneous -= 4 + (3 * random.random())


def eating(this_vars):
    """Check for illness based on quality of meals."""

    RND = random.random()
    if this_vars.choice_of_eating == 1:
        or78_helpers.illness(this_vars)
    elif this_vars.choice_of_eating == 3:
        if RND < 0.5:
            or78_helpers.illness(this_vars)
    else:
        if RND < 0.25:
            or78_helpers.illness(this_vars)


def animals_attack(this_vars):
    """Handle an attack by wild animals."""

    print("WILD ANIMALS ATTACK!")
    response_time = or78_helpers.shooting(this_vars.shooting_level)
    if this_vars.amount_spent_on_bullets <= 38:
        print("YOU WERE TOO LOW ON BULLETS--")
        print("THE WOLVES OVERPOWERED YOU")
        this_vars.is_injured = True
        this_vars.dead = True
        return

    if response_time <= 2:
        print("NICE SHOOTIN' PARDNER---THEY DIDN'T GET MUCH")
    else:
        print("SLOW ON THE DRAW---THEY GOT AT YOUR FOOD AND CLOTHES")
        this_vars.amount_spent_on_bullets -= 20 * response_time
        this_vars.amount_spent_on_clothing -= 4 * response_time
        this_vars.amount_spent_on_food -= 8 * response_time


def bandits_attack(this_vars):
    """Event triggered when bandits attack the party."""

    print("BANDITS ATTACK")
    response_time = or78_helpers.shooting(this_vars.shooting_level)
    this_vars.amount_spent_on_bullets -= 20 * response_time

    if this_vars.amount_spent_on_bullets < 0:
        print("YOU RAN OUT OF BULLETS---THEY GET LOTS OF CASH")
        this_vars.cash_total /= 3
        got_shot(this_vars)
    else:
        if response_time > 1:
            got_shot(this_vars)
        else:
            print("QUICKEST DRAW OUTSIDE OF DODGE CITY!!!")
            print("YOU GOT 'EM!")


# Events array

events_list = [
    weather,
    wagon_break_down,
    ox_injuries,
    arm_broke,
    ox_wander,
    helpful_indians,
    lost_son,
    unsafe_water,
    wagon_fire,
    heavy_fog,
    snake_poison,
    wagon_swamped,
    hail_storm,
    eating,
    animals_attack,
    bandits_attack,
]


def events(this_vars):
    """Choose and execute a random event."""

    ev = random.choice(events_list)
    ev(this_vars)
