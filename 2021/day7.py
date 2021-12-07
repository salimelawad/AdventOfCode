import numpy as np

input = np.array(list(map(int, open("day7.txt").read().splitlines()[0].split(","))))
median = np.median(input)

print(np.abs(input - median).sum())

minimun = min(input)
maximun = max(input)

print(
    min(
        [
            round(((np.abs((input - mean)) + 1) * (np.abs((input - mean)))).sum() / 2)
            for mean in range(minimun, maximun + 1)
        ]
    )
)
