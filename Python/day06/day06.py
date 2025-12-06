from Common import *


def mult(numbers):
    res = 1
    for n in numbers:
        res *= n
    return res


def calc(case):
    *numbers, op = case
    if op == "+":
        return sum(int(num) for num in numbers)
    else:
        return mult(int(num) for num in numbers)


def transform(data):
    cases = []
    left_pointer = 0
    max_cases = len(data[0].split())
    while len(cases) < max_cases:
        # Find longest number in column
        longest = max([len(line.split()[len(cases)]) for line in data])
        numbers = [""] * longest
        # Doesn't matter if we iterate left to right, addition and multiplication is commutative
        for number in range(longest):
            # Iterate over every row except operation and append a new digit (or space)
            for n in range(len(data) - 1):
                numbers[number] += data[n][left_pointer + number]
        op = data[-1][left_pointer]
        cases.append([*numbers, op])
        # Update where we are horizontally, accounting for length of longest number and space column separator
        left_pointer = left_pointer + longest + 1
    return cases


def solve1(data):
    return sum(calc(case) for case in data)


def solve2(data):
    return sum(calc(case) for case in transform(data))


# IO
a = input_as_lines("input.txt")
tokens = [line.split() for line in a]
cases = transpose(tokens)

# 1st
print(solve1(cases))

# 2nd
print(solve2(a))
