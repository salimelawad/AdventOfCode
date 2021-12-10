from itertools import combinations 
with open ("2020/data/day1.txt", "r") as myfile:
    data=myfile.read()

data = [int(x) for x in data.split("\n")]

comb = list(combinations(data, 3))

mult = [x+y+z for x,y,z in comb]

index = mult.index(2020)

print(comb[index][0] * comb[index][1] * comb[index][2])