nums = [10, 20, 4, 45, 99]
nums = list(set(nums))  # remove duplicates
nums.sort()
print("Second largest:", nums[-2])
