import itertools

number_map = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

input = [x.replace(" | ", " ") for x in open("day8.txt").read().splitlines()]
input = [x.split(" ") for x in input]

count = [0] * 7

for line in input:
    for digit in line[10:]:
        count[len(digit) - 1] += 1

print(sum(count[0:4] + count[6:]))

### PART 2 ####

n = "abcdefg"
needed = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
possible_mapping = list(map(lambda x: "".join(x), itertools.permutations(n, 7)))


def apply_mapping(input, mapping):
    new = []
    for x in input:
        mytable = x.maketrans(mapping, "abcdefg")
        new.append(x.translate(mytable))
    new = list(map(str, new))
    return new


def normalize(list_of_str):
    return ["".join(sorted(string)) for string in list_of_str]


number = []
for line in input:
    for aMap in possible_mapping:
        remapped = apply_mapping(line[0:10], aMap)
        if set(normalize(remapped)) == set(normalize(needed)):
            r = normalize(apply_mapping(line[10:], aMap))
            number.append(int("".join([number_map[x] for x in r])))

print(sum(number))
