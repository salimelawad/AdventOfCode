from collections import Counter

input = open("day6.txt").read().splitlines()[0].split(",")
input = [int(x) for x in input]


def next_day(lantern_dict):
    new_dict = {a: 0 for a in range(9)}
    for key, val in lantern_dict.items():
        if key >= 1:
            new_dict[key - 1] = new_dict[key - 1] + val
        else:
            new_dict[6] = new_dict[6] + val
            new_dict[8] = val
    return new_dict


c = {**{a: 0 for a in range(9)}, **Counter(input)}
print(c)
for i in range(256):
    c = next_day(c)

print(sum(c.values()))
