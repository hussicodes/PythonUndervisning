from random import random
from time import sleep


def state0():
    print("state0")
    # Sleep er en forsinkelse af programmet
    sleep(1.5)
    if random() >= .5:
        return state1
    else:
        return state2


def state1():
    print("state1")
    sleep(1.5)
    if random() >= .5:
        return state0
    else:
        return state2


def state2():
    print("state2")
    # Sleep er en forsinkelse af programmet
    sleep(1.5)
    if random() > .2:
        return state0
    else:
        return None


state = state0  # Første stadie
while state: 
    state = state()  # State machine kører
print("Done with states")
