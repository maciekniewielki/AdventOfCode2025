from Common import *


def get_rect(red1, red2):
    top_right = (max([red1[0], red2[0]]), max([red1[1], red2[1]]))
    bottom_left = (min([red1[0], red2[0]]), min([red1[1], red2[1]]))

    return bottom_left, top_right


def is_inside(red, rect):
    bottom_left, top_right = rect
    if (
        red[0] > bottom_left[0]
        and red[0] < top_right[0]
        and red[1] > bottom_left[1]
        and red[1] < top_right[1]
    ):
        return True
    return False


def area(rect):
    bottom_left, top_right = rect
    return (top_right[0] - bottom_left[0] + 1) * (top_right[1] - bottom_left[1] + 1)


# TODO Optimize this so that it goes one line at a time, not one step
def get_perimeter(red):
    current = red[0]
    for r in red[1:] + [red[0]]:
        diff = r[0] - current[0], r[1] - current[1]
        base_diff = sign(diff[0]), sign(diff[1])
        while current != r:
            yield current
            current = current[0] + base_diff[0], current[1] + base_diff[1]


def is_valid(rect, perimeter):
    for perim in perimeter:
        if is_inside(perim, rect):
            return False
    return True


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0


def solve1(data):
    max_area = 0
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            red1, red2 = data[i], data[j]
            rect = get_rect(red1, red2)
            if area(rect) > max_area:
                max_area = area(rect)
    return max_area


def solve2(red):
    rects = []
    for i in range(0, len(red) - 1):
        for j in range(i + 1, len(red)):
            red1, red2 = red[i], red[j]
            rect = get_rect(red1, red2)
            rects.append((rect, area(rect)))
    sorted_rects = sorted(rects, key=lambda r: r[1], reverse=True)
    perimeter = [x for x in get_perimeter(red)]
    for rect, r_area in sorted_rects:
        if is_valid(rect, perimeter):
            return r_area


# IO
a = input_as_lines("input.txt")
red = [tuple(int(coord) for coord in line.split(",")) for line in a]

# 1st
print(solve1(red))

# 2nd
print(solve2(red))
