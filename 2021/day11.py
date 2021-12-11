import pandas as pd
import numpy as np

input = [list(map(int, list(x))) for x in open("day11.txt").read().splitlines()]
array = np.array(input)
print(array)
"""You enter a large cavern full of rare bioluminescent dumbo octopuses! They seem to not like the Christmas lights on your submarine, so you turn them off for now.

There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and flashes brightly for a moment when its energy is full. Although your lights are off, maybe you could navigate through the cave without disturbing the octopuses if you could predict when the flashes of light will happen.

Each octopus has an energy level - your submarine can remotely measure the energy level of each octopus (your puzzle input). For example:

5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
The energy level of each octopus is a value between 0 and 9. Here, the top-left octopus has an energy level of 5, the bottom-right one has an energy level of 6, and so on.

You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash."""

def increase_adjacent(array, m, n):
    def increase_except_if_zero(num):
        if num == 0:
            return 0
        else:
            return 1
    max_m, max_n = array.shape
    if m > 0:
        array[m-1][n] += increase_except_if_zero(array[m-1][n])
    if m < max_m - 1:
        array[m+1][n] += increase_except_if_zero(array[m+1][n])
    if n > 0:
        array[m][n-1] += increase_except_if_zero(array[m][n-1])
    if n < max_n - 1:
        array[m][n+1] += increase_except_if_zero(array[m][n+1])
    if m > 0 and n > 0:
        array[m-1][n-1] += increase_except_if_zero(array[m-1][n-1])
    if m < max_m-1 and n < max_n-1:
        array[m+1][n+1] += increase_except_if_zero(array[m+1][n+1])
    if m > 0 and n < max_n-1:
        array[m-1][n+1] += increase_except_if_zero(array[m-1][n+1])
    if m < max_m - 1 and n > 0:
        array[m+1][n-1] += increase_except_if_zero(array[m+1][n-1])
    array[m][n] = 0
    return array

def check_more_flash(array):
    return np.count_nonzero(array > 9)

def return_indeces_of_9(array):
    i = np.where(array > 9)
    return list(zip(list(i[0]), list(i[1])))

def set_to_zero(array, indeces):
    for m, n in indeces:
        array[m,n] = 0
    return array

steps = 100
flashes = 0
for i in range(steps):
    array = array + 1
    max_m, max_n = array.shape
    set_to_flash = []
    while (check_more_flash(array) > 0):
        set_to_flash = set_to_flash + return_indeces_of_9(array)
        for m, n in return_indeces_of_9(array):
            array = increase_adjacent(array, m, n)
            flashes += 1
    array = set_to_zero(array, set_to_flash)



print(array)
print(flashes)


### PART 2 ###

input = [list(map(int, list(x))) for x in open("day11.txt").read().splitlines()]
array = np.array(input)
steps = 0
while(np.sum(array) > 0):
    steps = steps + 1
    array = array + 1
    max_m, max_n = array.shape
    set_to_flash = []
    while (check_more_flash(array) > 0):
        set_to_flash = set_to_flash + return_indeces_of_9(array)
        for m, n in return_indeces_of_9(array):
            array = increase_adjacent(array, m, n)
            flashes += 1
    array = set_to_zero(array, set_to_flash)

print(steps)


