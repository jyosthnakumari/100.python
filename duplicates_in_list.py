nums = [1, 2, 3, 2, 4, 1, 5]
duplicates = list(set([x for x in nums if nums.count(x) > 1]))
print("Duplicates:", duplicates)
