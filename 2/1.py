from itertools import pairwise

lines = [[int(c) for c in line.split()] for line in open("input.txt").readlines()]
safe_nr = len(lines)
for line in lines:
    sign = line[1] - line[0] > 0
    found_single_bad = False
    for n, n1 in pairwise(line):
        diff = n1 - n
        if sign != (diff > 0) or abs(diff) > 3 or abs(diff) < 1:
            if found_single_bad:
                safe_nr -= 1
                break
            found_single_bad = True

print(safe_nr)
