def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

lst = [5, 1, 4, 2, 8]
bubble_sort(lst)
print(lst)  # [1, 2, 4, 5, 8]
