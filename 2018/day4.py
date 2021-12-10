# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:57:23 2018

@author: elawa
"""

import pandas as pd
import numpy as np
from collections import Counter
import re 
with open("data/day4.txt") as file:
    data = file.read().split("\n")

data.sort()

clean_data = []

for row_index in range(len(data)):
    row = data[row_index]
    date = row[1:17]
    action = row[19:] 
    minute = int(date[-2:])
    clean_data.append({'date': date, 'action': action, 'minute': minute})
    
total_guard_dict = {}
total_guard_dict_awake = {}
for row_index in range(len(clean_data)):
    row = clean_data[row_index]
    date = row['date']
    action = row['action']
    minute = row['minute']
    
    guard_exist = re.search(r'([0-9]+)', action)
    if guard_exist is not None:
        guard=guard_exist.group(0)
        print('new guard ' + guard)
        if guard not in total_guard_dict.keys():
            total_guard_dict[guard] = [0 for x in range(60)]
            total_guard_dict_awake = [0 for x in range(60)]
    else:
        guard_exist = False
        
    if action == 'falls asleep':
        print(clean_data[row_index+1])
        for minutes in range(minute, clean_data[row_index+1]['minute']):
            total_guard_dict[guard][minutes] += 1
            
    if action == 'wakes up':
        pass
        

max_guard = 0
max_min= 0 
total_sleep = 0
for guard in total_guard_dict.keys():
#    if guard == '131':
    sleep = total_guard_dict[guard]
    for min in range(len(sleep)):
        if sleep[min] > total_sleep:
            max_guard = guard
            max_min = min
            total_sleep = sleep[min]
        
print(max_guard)
print(max_min)
print(total_sleep)

print(int(max_guard)*max_min)
    
for guard in total_guard_dict.keys():
    print(guard, sum(total_guard_dict[guard]))