import pandas as pd
from itertools import combinations 
with open ("2020/data/day10.txt", "r") as myfile:
    data=list(map(int, myfile.read().split("\n")))

data = data + [0, max(data)+3]
data = sorted(data)
diff = [data[i+1]-data[i] for i in range(len(data)-1)]
one = diff.count(1)
three = diff.count(3)
print(one*three)
#####
graph = {x: set([]) for x in data}

for i in data:
    for e in data:
        if i == e:
            break
        if abs(i-e) <= 3:
            graph[i].add(e)

paths = {}
def recursive(n):
    global paths
    if n in paths:
        return paths[n]
    if n == 0:
        return 1
    paths[n] = sum([recursive(x) for x in graph[n]])
    return paths[n]

recursive(max(data))
print(paths[max(data)])
