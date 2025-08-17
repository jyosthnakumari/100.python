lst = [1, 2, 2, 3, 4, 3, 2, 1]
freq = {}

for item in lst:
    freq[item] = freq.get(item, 0) + 1

print(freq)   # {1: 2, 2: 3, 3: 2, 4: 1}
