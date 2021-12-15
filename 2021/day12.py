txt = open("day12.txt").read().splitlines()

split = list(map(lambda x: x.split("-"), txt))


def build_graph(split):
    graph = {}
    for i, j in split:
        if graph.get(i) == None:
            graph[i] = set([])
        if graph.get(j) == None:
            graph[j] = set([])
        graph[i].add(j)
        graph[j].add(i)
    return graph


graph = build_graph(split)
visitedList = []


def dfs(path, graph, node, end):
    path = path + [node]
    if node == end:
        visitedList.append(path)
        return
    for neighbour in graph[node]:
        if neighbour not in path or neighbour.upper() == neighbour:
            dfs(path, graph, neighbour, end)


dfs([], graph, "start", "end")

print(len(visitedList))

## PART 2
visitedList = []


def dfs2(path, graph, node, end, double=False):
    path = path + [node]
    if node == end:
        visitedList.append(path)
        return
    for neighbour in graph[node]:
        if neighbour not in path or neighbour.upper() == neighbour:
            dfs2(path, graph, neighbour, end, double)
        elif (
            neighbour.lower() == neighbour
            and neighbour in path
            and double == False
            and neighbour not in ("start", "end")
        ):
            dfs2(path, graph, neighbour, end, True)


dfs2([], graph, "start", "end")

print(len(visitedList))

# print(set(list(map(tuple, visitedList))))
# print(len(set(list(map(tuple, visitedList)))))
