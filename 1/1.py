from collections import Counter

data = [line.split() for line in open("input.txt", "r").readlines()]
first = []
second = []
for a, b in data:
    first.append(int(a))
    second.append(int(b))
first = sorted(first)
second = sorted(second)
result = sum(abs(a - b) for a, b in zip(first, second))

c = Counter(second)
result2 = sum(num * c[num] for num in set(first))
print(result)
print(result2)
