from Common import *

import numpy as np
from scipy.optimize import linprog
from itertools import chain, combinations


class State:
    def __init__(self, init_state):
        self._init_state = [bool(x) for x in init_state]
        self.state = self._init_state[:]
        self.history = []

    def __str__(self):
        return " ".join([str(int(x)) for x in self.state])

    def reset_state(self):
        self.history = []
        self.state = self._init_state[:]

    def apply_transformations(self, t):
        for key in t:
            self.negate(t[key])
            self.history.append({key: t[key]})

    def negate(self, indexes):
        for index in indexes:
            self.state[index] = not self.state[index]

    def get_rotation_history(self):
        return [list(transformation.keys())[0] for transformation in self.history]


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))


def solve_state(state, possible_transformations, target):
    for subset in powerset(possible_transformations):
        state.reset_state()

        transformation = {}
        for trans in subset:
            transformation.update(trans)
        state.apply_transformations(transformation)
        if all(s == t for s, t in zip(state.state, target)):
            history = state.get_rotation_history()
            return history


def generate_possible_states(state, possible_transformations):
    possible_states = set()
    for subset in powerset(possible_transformations):
        state.reset_state()

        transformation = {}
        for trans in subset:
            transformation.update(trans)
        state.apply_transformations(transformation)
        possible_states.add(tuple(state.state))
    return possible_states


def to_tuple(b):
    return tuple(int(coord) for coord in b[1:-1].split(","))


def solve_machine(lights, buttons):
    initial_state = State([0] * len(lights))
    transformations = []
    for i, button in enumerate(buttons):
        transformations.append({i: button})
    history = solve_state(initial_state, transformations, lights)
    return len(history)


def solve_lin_alg(buttons, joltages):
    base_vectors = []
    for button in buttons:
        base_vectors.append([1 if x in button else 0 for x in range(len(joltages))])

    A_eq = np.array(base_vectors).T
    b_eq = np.array(joltages)
    c = np.ones(A_eq.shape[1])
    return sum(linprog(c, A_eq=A_eq, b_eq=b_eq, integrality=1, bounds=(0, None)).x)


def solve1(data):
    return sum(solve_machine(lights, buttons) for lights, buttons, _ in data)


def solve2(machines):
    return sum(int(solve_lin_alg(button, joltages)) for _, button, joltages in machines)


# IO
a = input_as_lines("input.txt")
machines = []
for line in a:
    lights, *buttons, joltage = line.split(" ")
    machines.append(
        (
            [1 if char == "#" else 0 for char in lights[1:-1]],
            [to_tuple(button) for button in buttons],
            to_tuple(joltage),
        )
    )


# 1st
print(solve1(machines))

# 2nd
print(solve2(machines))
