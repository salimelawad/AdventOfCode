# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 23:07:11 2018

@author: elawa
"""
### PART 1

with open("data/day1.txt") as file:
    data = file.read().split("\n")
    
data = [int(x) for x in data]

print(sum(data))

### PART 2

freq_hist = set([0])

freq = 0

run=True

while(run):
    for freq_change in data:
        freq = freq + freq_change
        
        if freq in freq_hist:
            print(freq)
            run=False
            break
    
        else:
            freq_hist.add(freq)

