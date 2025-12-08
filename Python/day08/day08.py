from Common import *
import math


def calc_dist(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2)


def calc_top_3(circuits):
    s = sorted(get_unique(circuits), key=lambda c: len(c), reverse=True)
    m = 1
    for c, _ in zip(s, range(3)):
        m *= len(c)
    return m


def get_unique(circuits):
    unique_circuits = []
    for c in circuits.values():
        if c in unique_circuits:
            continue
        unique_circuits.append(c)
    return unique_circuits


def connect_one(circuits, sorted_dists):
    j1, j2, _ = sorted_dists.pop(0)
    if j1 in circuits and j2 in circuits:
        c1 = circuits[j1]
        c2 = circuits[j2]
        if c1 == c2:
            # Both are in the same circuit, nothing to do
            return j1, j2

        # Make all junctions in c2 map to circuit 1 and join them
        for junction2 in c2:
            circuits[junction2] = c1
        c1.extend(c2)
        return j1, j2

    if j1 in circuits:
        # Connect j2 to existing j1 circuit
        circuit = circuits[j1]
        circuit.append(j2)
        circuits[j2] = circuit
    elif j2 in circuits:
        # Connect j1 to existing j2 circuit
        circuit = circuits[j2]
        circuit.append(j1)
        circuits[j1] = circuit
    else:
        # Create a new circuit for j2 and j2
        new_circuit = [j1, j2]
        circuits[j1] = new_circuit
        circuits[j2] = new_circuit
    return j1, j2


def solve1(data):
    circuits = {}
    dists = [
        (data[i], data[j], calc_dist(data[i], data[j]))
        for i in range(len(data) - 1)
        for j in range(i + 1, len(data))
    ]
    sorted_dists = sorted(dists, key=lambda d: d[2])
    for _ in range(1000):
        connect_one(circuits, sorted_dists)

    return calc_top_3(circuits)


def solve2(data):
    circuits = {}
    dists = [
        (data[i], data[j], calc_dist(data[i], data[j]))
        for i in range(len(data) - 1)
        for j in range(i + 1, len(data))
    ]
    sorted_dists = sorted(dists, key=lambda d: d[2])
    while len(circuits) == 0 or len(next(iter(circuits.values()))) < len(data):
        j1, j2 = connect_one(circuits, sorted_dists)

    return j1[0] * j2[0]


# IO
a = input_as_lines("input.txt")
junctions = [tuple(int(coord) for coord in line.split(",")) for line in a]

# 1st
print(solve1(junctions))

# 2nd
print(solve2(junctions))
