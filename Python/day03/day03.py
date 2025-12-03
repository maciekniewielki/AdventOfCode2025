from Common import *


def max_battery_index(battery, max_i=9):
    for i in range(max_i, 0, -1):
        digit = str(i)
        if digit in battery:
            return battery.index(digit)


def max_joltage(bank, n):
    if n == 1:
        index = max_battery_index(bank)
        return bank[index]

    for i in range(9, 0, -1):
        index = max_battery_index(bank, i)
        # Not enough space left
        if len(bank) < index + n:
            continue
        return bank[index] + max_joltage(bank[index + 1 :], n - 1)


def solve1(data):
    return sum(int(max_joltage(case, 2)) for case in data)


def solve2(data):
    return sum(int(max_joltage(case, 12)) for case in data)


# IO
a = input_as_lines("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
