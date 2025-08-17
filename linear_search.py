def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i   # returns index
    return -1

numbers = [5, 8, 2, 9, 3]
print(linear_search(numbers, 9))   # 3
print(linear_search(numbers, 7))   # -1
