from Common import *


def removable(grid, y, x):
    if not grid[y][x] == "@":
        return False
    neighbors = sum(
        1 if neighbor == "@" else 0
        for neighbor in grid_neighbors(grid, y, x, diagonal=True)
    )
    return neighbors < 4


def solve1(grid):
    return sum(1 if removable(grid, y, x) else 0 for y, x in grid_iterate(grid))


def solve2(grid):
    removed = True
    total = 0
    while removed:
        removed = False
        for y, x in grid_iterate(grid):
            if removable(grid, y, x):
                grid[y][x] = "."
                removed = True
                total += 1
    return total


# IO
a = input_as_2d_grid("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
