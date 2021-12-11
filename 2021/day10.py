import pprint
import numpy as np
import statistics
pp = pprint.PrettyPrinter(width=100, compact=True)


input = open("day10.txt").read().splitlines()


value = {')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
        }

def process_line(line):
    stack = []
    open = list('{[<(')
    close = {'}':'{', ']':'[', ')':'(', '>':'<'}
    for c in line:
        if c in open:
            stack.append(c)
        else:
            out = stack.pop()
            if out != close[c]:
                return c

bad_chars = []
for line in input:
    if process_line(line):
        bad_chars.append(process_line(line))

print(sum(list(map(lambda x: value[x], bad_chars))))

### part 2 ####

def fix_line(line):
    stack = []
    open = list('{[<(')
    close = {'}':'{', ']':'[', ')':'(', '>':'<'}
    open = {'{':'}', '[':']', '(':')', '<':'>'}
    for c in line:
        if c in open:
            stack.append(c)
        else:
            out = stack.pop()
            if out != close[c]:
                pass
    return list(reversed(list(map(lambda x: open[x], stack))))

value2 = {')': 1,
        ']': 2,
        '}': 3,
        '>': 4
        }

bad_strings = []
for line in input:
    if process_line(line) is None:
        print(fix_line(line))
        bad_strings.append(fix_line(line))

def calc_bad_strings(string):
    val = 0
    for i in string:
        val = val * 5
        val = val + value2[i]
    return val

total_scores = []
for line in bad_strings:
    print(calc_bad_strings(line))
    total_scores.append(calc_bad_strings(line))

print(list(map(lambda x: "".join(x), bad_strings)))

print(statistics.median((total_scores)))