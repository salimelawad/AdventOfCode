# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:59:23 2018

@author: elawa
"""

import pandas as pd
import numpy as np
import nltk

with open("data/day2.txt") as file:
    data = file.read().split("\n")
    
num_of_2 = 0
num_of_3 = 0
    
for row in data:
    count_dict = {}
    for letter in row:
        if letter not in count_dict:
            count_dict[letter]=1
        else:
            count_dict[letter]=count_dict[letter]+1
    
    count_list = list(count_dict.values())
    
    if 2 in count_list:
        num_of_2 = num_of_2 + 1
        
    if 3 in count_list:
        num_of_3 = num_of_3 + 1
        
print(num_of_2*num_of_3)


#### Part 2
solution1 = ""
solution2 = ""
for row in data:
    for row2 in data:
        if nltk.edit_distance(row, row2) == 1:
            solution1 = row
            solution2 = row2
            
solution = [solution1[i] for i in range(len(solution1)) if solution1[i]==solution2[i]]
print("".join(solution))
