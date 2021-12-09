import pprint
import numpy as np

pp = pprint.PrettyPrinter(width=100, compact=True)
input = [list(map(int, list(x))) for x in open("day9.txt").read().splitlines()]
pp.pprint(input)

array = np.array(input)
print(array)


def check(m, n, array):
    m_len, n_len = array.shape
    up = (m - 1, n)
    down = (m + 1, n)
    right = (m, n + 1)
    left = (m, n - 1)
    up_val = None
    down_val = None
    right_val = None
    left_val = None
    if up[0] >= 0 and up[0] < m_len:
        up_val = array[up[0]][up[1]]
    if down[0] >= 0 and down[0] < m_len:
        down_val = array[down[0]][down[1]]
    if right[1] >= 0 and right[1] < n_len:
        right_val = array[right[0]][right[1]]
    if left[1] >= 0 and left[1] < n_len:
        left_val = array[left[0]][left[1]]

    current = array[m][n]

    bools = np.array(
        [
            (up_val is None or up_val > current),
            (down_val is None or down_val > current),
            (right_val is None or right_val > current),
            (left_val is None or left_val > current),
        ]
    )
    return bools.all()


lows = []
for m in range(array.shape[0]):
    for n in range(array.shape[1]):
        if check(m, n, array):
            lows.append(array[m, n])

print(sum(lows) + len(lows))

#### Part 2 ####

basin = np.zeros(array.shape, dtype=int)
basin_count = 1
for m in range(array.shape[0]):
    for n in range(array.shape[1]):
        if check(m, n, array):
            basin[m, n] = basin_count
            basin_count += 1


def adj_to_basin(m, n, basin, matrix):
    if matrix[m, n] == 9:
        return 0
    m_len, n_len = basin.shape
    up = (m - 1, n)
    down = (m + 1, n)
    right = (m, n + 1)
    left = (m, n - 1)
    up_val = None
    down_val = None
    right_val = None
    left_val = None
    if up[0] >= 0 and up[0] < m_len:
        up_val = basin[up[0]][up[1]]
    if down[0] >= 0 and down[0] < m_len:
        down_val = basin[down[0]][down[1]]
    if right[1] >= 0 and right[1] < n_len:
        right_val = basin[right[0]][right[1]]
    if left[1] >= 0 and left[1] < n_len:
        left_val = basin[left[0]][left[1]]

    if up_val is not None and up_val != 0:
        return up_val
    if down_val is not None and down_val != 0:
        return down_val
    if right_val is not None and right_val != 0:
        return right_val
    if left_val is not None and left_val != 0:
        return left_val
    return 0


print(basin)

flag = True
while flag:
    flag = False
    for m in range(array.shape[0]):
        for n in range(array.shape[1]):
            if basin[m, n] != 0:
                continue
            else:
                if adj_to_basin(m, n, basin, array) != 0:

                    flag = True
                    basin[m, n] = adj_to_basin(m, n, basin, array)

print(basin)
sizes = sorted([np.count_nonzero(basin == i) for i in range(basin_count)][1:], reverse=True)[0:3]
print(sizes)
# multply product of list called sizes
print(np.product(sizes))
