import pandas as pd
import numpy as np

file1 = open('day1.csv', 'r')
lines = [int(x) for x in file1.readlines()]

def aFunc(x, aList):
    if aList[x] < aList[x+1]:
        return 1
    return 0

increases = [aFunc(x, lines) for x in range(len(lines)-1)]
print(sum(increases))

#### PART 2 #####

aList = []
for i in range(len(lines)-2):
    aList.append(sum(lines[i:i+3]))
    
increases2 = [aFunc(x, aList) for x in range(len(aList)-1)]
print(sum(increases2))