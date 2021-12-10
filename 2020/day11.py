import pandas as pd
import pprint
import time
from copy import deepcopy
from itertools import combinations, product
with open ("2020/data/day11.txt", "r") as myfile:
    data=myfile.read().split("\n")
pp = pprint.PrettyPrinter(indent=4)

def get_adjacent_seats(i,j,data):
    seats = list(product((i-1, i, i+1),(j-1, j, j + 1)))
    seats.remove((i,j))
    return [(ii,jj) for ii,jj in seats if ii>=0 and jj>=0 and ii < len(data) and jj < len(data[0])]

def count_occupied(i,j,data):
    adj_list = get_adjacent_seats(i,j,data)
    count = 0
    for i,j in adj_list:
        if data[i][j] == '#':
            count = count + 1
    return count

def update(i,j,data):
    seat = data[i][j]
    if seat == '.':
        return '.'
    num_occupied = count_occupied(i,j,data)
    if seat =='L' and num_occupied == 0:
        return '#'
    if seat =='#' and num_occupied >= 4:
        return 'L'
    return seat

def compare_datasets(old, new):
    assert len(old)==len(new)
    assert len(old[0])==len(new[0])
    flag= True
    for i in range(len(old)):
        if old[i] != new[i]:
            flag = False
    return flag

# recurse until fix
count = 0
new_data = deepcopy(data)
while(True):
    count = count+1
    # print(count)
    old_data = deepcopy(new_data)
    new_data = []
    for i in range(len(old_data)):
        strrow=''
        for j in range(len(old_data[i])):
            strrow = strrow+update(i,j,old_data)
        new_data.append(strrow)
    # pp.pprint(new_data)
    # print(sum([i.count('.') for i in new_data]))
    # print(sum([i.count('L') for i in new_data]))
    # print(sum([i.count('#') for i in new_data]))
    if compare_datasets(old_data, new_data):
        break

########

def normalize(n):
    if n == 0:
        return 0
    if n > 0:
        return 1
    if n < 0:
        return -1

def get_adjacent_seats(i,j,data):
    seats = list(product((i-1, i, i+1),(j-1, j, j + 1)))
    seats.remove((i,j))
    return [(ii,jj) for ii,jj in seats if ii>=0 and jj>=0 and ii < len(data) and jj < len(data[0])]

def count_occupied(i,j,data):
    adj_list = get_adjacent_seats(i,j,data)
    count = 0
    for ii,jj in adj_list:
        while(True):
            ii,jj = ii,jj
            if data[ii][jj] == '#':
                count = count + 1
                break
            if data[ii][jj] == '.':
   
                row_diff = normalize(ii-i)
                col_diff = normalize(jj-j)

                ii,jj = ii + row_diff, jj + col_diff
                if ii>=0 and jj>=0 and ii < len(data) and jj < len(data[0]):
          
                    continue
                else:
                    break
            break
    return count

def update(i,j,data):
    seat = data[i][j]
    if seat == '.':
        return '.'
    num_occupied = count_occupied(i,j,data)
    if seat =='L' and num_occupied == 0:
        return '#'
    if seat =='#' and num_occupied >= 5:
        return 'L'
    return seat

def compare_datasets(old, new):
    assert len(old)==len(new)
    assert len(old[0])==len(new[0])
    flag= True
    for i in range(len(old)):
        if old[i] != new[i]:
            flag = False
    return flag

# recurse until fix
print("second_start")
count = 0
new_data = deepcopy(data)
while(True):
    count = count+1
    print(count)
    old_data = deepcopy(new_data)
    new_data = []
    for i in range(len(old_data)):
        strrow=''
        for j in range(len(old_data[i])):
            strrow = strrow+update(i,j,old_data)
        new_data.append(strrow)
    pp.pprint(new_data)
    # print(sum([i.count('.') for i in new_data]))
    # print(sum([i.count('L') for i in new_data]))
    print(sum([i.count('#') for i in new_data]))
    if compare_datasets(old_data, new_data):
        break

