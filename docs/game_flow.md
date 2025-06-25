# Game Flow

This document outlines the high level flow of the Python port of **The Oregon Trail**.
The program is split across several modules and a central `GameGlobals` object that
tracks game state. Functions from the modules are called in sequence from `or78.game()`
which coordinates the entire run.

## Modules

- `or78_vars` – defines `GameGlobals` which stores all mutable game state.
- `or78_1_intro` – handles the introduction and initial purchasing phase via `init`.
- `or78_2_date` – utilities for printing the current game date.
- `or78_3_loop` – core turn logic (`begin`, `choices`, `toggle_fort_presence`, `eating`).
- `or78_4_riders` – encounters with approaching riders.
- `or78_5_events` – random events that affect supplies and health.
- `or78_6_mountain` – mountain pass challenges and blizzards.
- `or78_7_endings` – final turn calculations and death handling.
- `or78_helpers` – helper input and shooting utilities used throughout the game.

## Flow Diagram

```mermaid
flowchart TD
    start([Start or78.game]) --> globals[[GameGlobals]]
    globals --> intro[init (or78_1_intro)]
    intro --> loop{Turn Loop}

    loop --> date[print_date]
    date --> begin[begin]
    begin --> choices[choices]
    choices --> toggle[toggle_fort_presence]
    toggle --> eat[eating]
    eat --> riders
    riders --> events
    events --> mountain
    mountain --> checkGoal{Reached goal?}

    checkGoal -- yes --> final[final_turn]
    checkGoal -- no --> inc[increment_turn]
    inc --> tooLate{no_turns_left?}
    tooLate -- yes --> timeout[print_too_long]
    timeout --> death
    tooLate -- no --> loop

    loop --> |dead at any step| death[death]
    final --> end([END])
    death --> end
```
