import pandas as pd
from itertools import combinations 
with open ("2020/data/day10_sample.txt", "r") as myfile:
    data=list(map(int, myfile.read().split("\n")))

data = data + [0, max(data)+3]
data = sorted(data)
print(data)
diff = [data[i+1]-data[i] for i in range(len(data)-1)]
print(diff)
one = diff.count(1)
three = diff.count(3)
print(one*three)

path_count = [0 for x in data]
# for i in range(len(data)):
#     plug = data[(i)]
#     if plug-1 in path_count:
#         path_count[plug] = path_count[plug] + path_count[plug-1] + 1
#     if plug-3 in path_count:
#         path_count[plug] = path_count[plug] + path_count[plug-3] + 1
#     if plug +3 in path_count:
#         path_count[plug] = path_count[plug]+1
#     if plug +1 in path_count:
#         path_count[plug] = path_count[plug]+1

# print(path_count)

# graph = {x: set([]) for x in data}

# for i in data:
#     if (i + 1) in graph:
#         graph[i].add(i + 1)
#     if (i + 3) in graph:
#         graph[i].add(i + 3)

# print(graph)

data_set = set(data)

for i in data_set: