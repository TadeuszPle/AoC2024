data = open("input.txt").read()
# get all valid mult(num,num)
import re

data2 = []

dont_indexes = re.finditer(r"don't\(\)", data)
do_indexes = list(re.finditer(r"do\(\)", data))[::-1]
prev_end = 0
for span in dont_indexes:
    start = span.span()[0]
    if start < prev_end:  # more than one don't in a row
        continue
    if not do_indexes:  # no more do's
        prev_end = len(data)
        break
    while do_indexes:
        stop = do_indexes.pop().span()[1]
        if stop > start:
            break
    data2.append(data[prev_end:start])
    print(data[prev_end:start])
    prev_end = stop

data2 = "".join(data2)
open("data2.txt", "w").write(data2)
pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, data)
matches2 = re.findall(pattern, data2)
just_numbers = [match[4:-1].split(",") for match in matches]
just_numbers2 = [match[4:-1].split(",") for match in matches2]
result = sum(int(a) * int(b) for a, b in just_numbers)
result2 = sum(int(a) * int(b) for a, b in just_numbers2)
print(result, result2)
