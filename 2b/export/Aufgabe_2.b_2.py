"""
Traffic Light State Machine
Assignment 2b - INF2556 Game Development

A finite state machine that simulates a traffic light cycling
automatically between Green, Yellow, and Red states using a timer.
"""

import time
from enum import Enum


class State(Enum):
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"


# Duration of each state (in seconds)
STATE_DURATIONS = {
    State.GREEN: 5.0,
    State.YELLOW: 2.0,
    State.RED: 5.0,
}

# Transition table: current state -> next state
TRANSITIONS = {
    State.GREEN: State.YELLOW,
    State.YELLOW: State.RED,
    State.RED: State.GREEN,
}

# Visual representation for each state (ANSI color codes for the terminal)
STATE_DISPLAY = {
    State.GREEN:  ("\033[92m", "GREEN  - GO"),          # Bright green
    State.YELLOW: ("\033[93m", "YELLOW - SLOW DOWN"),   # Bright yellow
    State.RED:    ("\033[91m", "RED    - STOP"),       # Bright red
}
RESET = "\033[0m"


def enter_state(state: State) -> None:
    """Display the behavior associated with the given state."""
    color, message = STATE_DISPLAY[state]
    print(f"{color}[{state.value}] {message}{RESET}")


def change_state(current: State) -> State:
    """Return the next state based on the transition table."""
    return TRANSITIONS[current]


def run_state_machine(cycles: int = 3) -> None:
    """
    Run the traffic light state machine for a given number of cycles.
    One cycle = Green -> Yellow -> Red.
    """
    current_state = State.GREEN
    total_transitions = cycles * 3  # 3 states per cycle

    enter_state(current_state)

    for _ in range(total_transitions):
        # Wait for the current state's duration before transitioning
        time.sleep(STATE_DURATIONS[current_state])
        current_state = change_state(current_state)
        enter_state(current_state)


if __name__ == "__main__":
    print("=== Traffic Light State Machine ===\n")
    run_state_machine(cycles=3)
    print("\n=== End of simulation ===")