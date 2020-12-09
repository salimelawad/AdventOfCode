# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 23:55:41 2018

@author: elawa
"""

import pandas as pd
import numpy as np
import nltk
from collections import Counter


### Part 1

with open("data/day3.txt") as file:
    data = file.read().split("\n")

data_format = []
for row in data:
    r = row.split(" ")
    r = r[2:]
    r[0] = r[0][:-1].split(',')
    r[1] = r[1].split('x')
    r[0][0] = int(r[0][0])
    r[0][1] = int(r[0][1])
    r[1][0] = int(r[1][0])
    r[1][1] = int(r[1][1])
    data_format.append(r)
    
    
fabric = np.zeros((1000,1000))

for row in data_format:
    for horizontal in range(row[1][0]):
        for vertical in range(row[1][1]):
            fabric[vertical+row[0][1], horizontal + row[0][0]] += 1
            
total = len(fabric[fabric > 1])

print("Part 1: ", total)
            

### Part 2

for super_row_index in range(len(data_format)):
    fabric = np.zeros((1000,1000))
    super_row = data_format[super_row_index]
    overlap = False
    for row_index in range(len(data_format)):
        row = data_format[row_index]
        if row_index != super_row_index:
            for horizontal in range(row[1][0]):
                for vertical in range(row[1][1]):
                    fabric[vertical+row[0][1], horizontal + row[0][0]] += 1
    for horizontal in range(super_row[1][0]):
        for vertical in range(super_row[1][1]):
            if fabric[vertical+super_row[0][1], horizontal + super_row[0][0]] != 0:
                overlap = True
    
    if (overlap == False):
        perfect_row = super_row
        print("Part 2: ", total)
        print(super_row_index + 1)
        print(perfect_row)
        break