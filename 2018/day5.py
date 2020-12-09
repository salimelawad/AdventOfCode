# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:56:56 2018

@author: elawa
"""

import pandas as pd
import numpy as np
import nltk
from collections import Counter
import string


### Part 1
with open("data/day5.txt") as file:
    data = file.read()

done = False

#data = 'dabAcCaCBAcCcaDA'

print(len(data))
    
pattern = []
for i in string.ascii_lowercase:
    pattern.append(i+i.upper())
    pattern.append(i.upper()+i)


old_len = len(data)
while(True):
    print(len(data))
    for p in pattern:
        data = data.replace(p, '')
    if old_len  == len(data):
        break
    old_len = len(data)
    
print(len(data))


letter = 'r'
min_size = 10000000
# part 2
for letter_to_remove in string.ascii_lowercase:
    with open("data/day5.txt") as file:
        data = file.read()
    data = data.replace(letter_to_remove, '')
    data = data.replace(letter_to_remove.upper(), '')
    while(True):
        print(len(data))
        for p in pattern:
            data = data.replace(p, '')
        if old_len  == len(data):
            break
        old_len = len(data)
       
    if min_size>len(data):
        letter=letter_to_remove
        min_size=len(data)
    print(len(data))