my_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)   # [1, 2, 3, 4, 5]
