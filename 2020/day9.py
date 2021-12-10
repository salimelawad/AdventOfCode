from itertools import combinations 
with open ("2020/data/day9.txt", "r") as myfile:
    data=myfile.read()

int_data = list(map(int, data.split('\n')))

def is_sum(prefix, num):
    comb = list(combinations(prefix, 2))
    comb = [(x,y) for x,y in comb if x != y]
    return len([True for x,y in comb if x+y == num]) > 0

for i in range(len(int_data)-25):
    if is_sum(int_data[i:i+25], int_data[i+25]) == False:
        print(int_data[i+25])
        print(i+25, int_data[i+25])
        break

# part 2

for cont in range(1000):
    for i in range(1000-cont):
        if sum(int_data[i:i+cont]) == 26796446:
            print(int_data[i:i+cont])
            print(min(int_data[i:i+cont]) + max(int_data[i:i+cont]))