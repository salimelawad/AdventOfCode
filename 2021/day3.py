from statistics import mode
from collections import Counter


def bit_max(aList):
    c = Counter(aList)
    if c["0"] > c["1"]:
        return "0"
    elif c["0"] < c["1"]:
        return "1"
    else:
        return "1"


input = open("day3.txt").read().splitlines()
gamma = ""
epsilon = ""
for i in range(len(input[0])):
    most_common = mode([x[i] for x in input])
    gamma = gamma + most_common
    epsilon = epsilon + ("0" if most_common == "1" else "1")


print(int(gamma, 2) * int(epsilon, 2))

## PART 2 ##


def filter(data, current_position, flip_bit=False):
    if len(data) == 1:
        return data[0]

    bit = bit_max([x[current_position] for x in data])
    if flip_bit:
        bit = "0" if bit == "1" else "1"
    return filter(
        [x for x in data if x[current_position] == bit],
        current_position + 1,
        flip_bit=flip_bit,
    )


oxygen = filter(input, 0)
co2 = filter(input, 0, True)
print(int(oxygen, 2) * int(co2, 2))
