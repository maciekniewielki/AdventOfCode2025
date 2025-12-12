from Common import *


def solve_one(presents, case):
    height, width = case[0]
    presents_counts = case[1]
    all_nums = set()
    while any([count > 0 for count in presents_counts]):
        inserted = False
        for i, present_count in enumerate(presents_counts):
            if inserted:
                break
            if present_count == 0:
                continue
            for variant in presents[i]:
                offset_nums = fit_variant(height, width, all_nums, variant)
                if offset_nums:
                    all_nums |= offset_nums
                    presents_counts[i] -= 1
                    inserted = True
                    break
        if not inserted:
            break
    if any([count > 0 for count in presents_counts]):
        return 0
    return 1


def fit_variant(height, width, all_nums, variant):
    for h_offset in range(height - 2):
        for w_offset in range(width - 2):
            variant_offset = frozenset((y + h_offset, x + w_offset) for y, x in variant)
            if len(all_nums & variant_offset) == 0:
                return variant_offset
    return False


def solve1(presents, cases):
    return sum(solve_one(presents, case) for case in cases)


# IO
def convert_to_nums(present):
    nums = set()
    for y, x in grid_iterate(present):
        if present[y][x] == "#":
            nums.add((y, x))
    return frozenset(nums)


rotation90 = {
    (0, 0): (0, 2),
    (0, 1): (1, 2),
    (0, 2): (2, 2),
    (1, 0): (0, 1),
    (1, 1): (1, 1),
    (1, 2): (2, 1),
    (2, 0): (0, 0),
    (2, 1): (1, 0),
    (2, 2): (2, 0),
}


def get_variants_rotation(nums):
    rotated90 = frozenset(rotation90[pair] for pair in nums)
    rotated180 = frozenset(rotation90[pair] for pair in rotated90)
    rotated270 = frozenset(rotation90[pair] for pair in rotated180)
    return [rotated90, rotated180, rotated270]


def get_variants_flipped(nums):
    flipped_hor = frozenset((y, 2 - x) for y, x in nums)
    flipped_vert = frozenset((2 - y, x) for y, x in nums)
    return [flipped_hor, flipped_vert]


def get_variants(nums):
    all_variants = set()
    base_variants = [nums, *get_variants_flipped(nums)]
    for base in base_variants:
        all_variants.add(base)
        for rot in get_variants_rotation(base):
            all_variants.add(rot)
    return all_variants


a = input_as_chunks("input.txt")
presents = []
for present in a[:-1]:
    number, *shape = present
    nums = convert_to_nums([list(line) for line in shape])
    presents.append(get_variants(nums))

cases = []
for case in a[-1]:
    size, rest = case.split(": ")
    width, height = [int(side) for side in size.split("x")]
    numbers = [int(present_num) for present_num in rest.split(" ")]
    cases.append(((height, width), numbers))


# 1st
print(solve1(presents, cases))
