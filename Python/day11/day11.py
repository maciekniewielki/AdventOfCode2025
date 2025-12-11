from Common import *


def traverse(device, in_out, path):
    path.append(device)
    if device == "out":
        return [path]
    if len(path) > len(in_out):
        return []
    outputs = in_out[device]
    all_paths = []
    for out in outputs:
        for inner_path in traverse(out, in_out, path[:]):
            if len(inner_path) > 0:
                all_paths.append(inner_path)
    return all_paths


def count_paths(device, in_out, final, cache):
    if (device, final) in cache:
        return cache[(device, final)]
    if device == final:
        count = 1
    elif device not in in_out:
        count = 0
    else:
        count = sum(count_paths(next_device, in_out, final, cache) for next_device in in_out[device])
    cache[(device, final)] = count
    return count


def solve1(in_out):
    all_paths = traverse("you", in_out, [])
    return len(all_paths)


def solve2(in_out):
    cache = {}
    svr_fft = count_paths("svr", in_out, "fft", cache)
    svr_dac = count_paths("svr", in_out, "dac", cache)
    fft_dac = count_paths("fft", in_out, "dac", cache)
    dac_fft = count_paths("dac", in_out, "fft", cache)
    fft_out = count_paths("fft", in_out, "out", cache)
    dac_out = count_paths("dac", in_out, "out", cache)
    return svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out


# IO
a = input_as_lines("input.txt")
in_out = {}
for line in a:
    input, output = line.split(": ")
    in_out[input] = set(output.split(" "))

# 1st
print(solve1(in_out))

# 2nd
print(solve2(in_out))
