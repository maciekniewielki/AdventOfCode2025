from Common import *


def mod100(n):
    return (n + 100) % 100


def turn(current, direction, amount):
    current = mod100(current + direction * amount)
    return current, int(current == 0)


def turn_slow(current, direction, amount):
    total = 0
    for _ in range(amount):
        current = mod100(current + direction)
        if current == 0:
            total += 1
    return current, total


def run(data, turn_and_count):
    current = 50
    total = 0
    for direction, amount in data:
        current, zeros = turn_and_count(current, direction, amount)
        total += zeros
    return total


def solve1(data):
    return run(data, turn)


def solve2(data):
    return run(data, turn_slow)


# IO
a = input_as_lines("input.txt")
direction = {"R": 1, "L": -1}
data = [(direction[line[0]], int(line[1:])) for line in a]

# 1st
print(solve1(data))

# 2nd
print(solve2(data))
