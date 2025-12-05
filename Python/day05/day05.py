from Common import *


def merge_ranges(range1, range2):
    # Disjoint
    if range1[0] < range2[0] and range1[1] < range2[0]:
        return False
    if range1[0] > range2[1] and range1[1] > range2[1]:
        return False

    # One inside the other
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        return range1
    if range2[0] <= range1[0] and range2[1] >= range1[1]:
        return range2

    # Partial overlap
    if range1[0] <= range2[0] <= range1[1] and range2[1] >= range1[1]:
        return (range1[0], range2[1])
    if range2[0] <= range1[0] <= range2[1] and range1[1] >= range2[1]:
        return (range2[0], range1[1])


def try_merge(fresh):
    for i in range(len(fresh) - 1):
        for j in range(i + 1, len(fresh)):
            result = merge_ranges(fresh[i], fresh[j])
            if result:
                fresh.pop(j)
                fresh.pop(i)
                fresh.append(result)
                return True
    return False


def is_fresh(fresh, ingredient):
    for low, high in fresh:
        if low <= ingredient <= high:
            return True
    return False


def solve1(fresh, ingredients):
    return sum(1 if is_fresh(fresh, ingredient) else 0 for ingredient in ingredients)


def solve2(fresh):
    while try_merge(fresh):
        pass
    return sum(high - low + 1 for low, high in fresh)


# IO
a = input_as_chunks("input.txt")
fresh = []
for line in a[0]:
    low, high = line.split("-")
    fresh.append((int(low), int(high)))

ingredients = [int(line) for line in a[1]]

# 1st
print(solve1(fresh, ingredients))

# 2nd
print(solve2(fresh))
