with open ("2020/data/day2.txt", "r") as myfile:
    data=myfile.read()

data = data.split('\n')

data2 = [x.split(' ') for x in data]

# print(data2)

good1 = 0

for x in data2:
    low, high = [int(a) for a in x[0].split('-')]
    letter = x[1][0]
    string = x[2]
    count = string.count(letter)
    if count >= low and count <= high:
        good1 = good1 + 1

print(good1)

### part 2
good2 = 0
for x in data2:
    idx1, idx2 = [int(a)-1 for a in x[0].split('-')]
    letter = x[1][0]
    string = x[2]
    if string[idx1] == letter or string[idx2] == letter:
        if not (string[idx1] == letter and string[idx2] == letter):
            good2 = good2 + 1

print(good2)