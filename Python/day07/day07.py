from Common import *
from collections import defaultdict


def solve1(data):
    start = data[0].index("S")
    beams_positions = {start}
    total_splits = 0
    for line in data[1:]:
        possible_splits = {i for i, char in enumerate(line) if char == "^"}
        splits = possible_splits & beams_positions
        beams_positions |= {new_split for x in splits for new_split in {x - 1, x + 1}}
        beams_positions -= splits
        total_splits += len(splits)
    return total_splits


def solve2(data):
    start = data[0].index("S")
    beam_paths = defaultdict(int, {start: 1})
    for line in data[1:]:
        possible_splits = {i for i, char in enumerate(line) if char == "^"}
        splits = possible_splits & {*beam_paths}
        for x in splits:
            beam_paths[x - 1] += beam_paths[x]
            beam_paths[x + 1] += beam_paths[x]
            del beam_paths[x]
    return sum(beam_paths.values())


# IO
a = input_as_2d_grid("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
