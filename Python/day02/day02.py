from Common import *
import re

regexTwice = r"^(\d+)\1{1}$"
regexTwiceOrMore = r"^(\d+)\1+$"


def is_invalid(num, regex):
    return re.match(regex, str(num))


def find_invalid(low, high, regex):
    return sum(num for num in range(low, high + 1) if is_invalid(num, regex))


def solve1(data):
    return sum(find_invalid(low, high, regexTwice) for low, high in data)


def solve2(data):
    return sum(find_invalid(low, high, regexTwiceOrMore) for low, high in data)


# IO
a = input_as_string("input.txt")
cases = []
for case in a.split(","):
    low, high = case.split("-")
    cases.append((int(low), int(high)))


# 1st
print(solve1(cases))

# 2nd
print(solve2(cases))
