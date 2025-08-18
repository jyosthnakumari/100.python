def count_even_odd(nums):
    evens = odds = 0
    for x in nums:
        if x % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

# Example
nums = [2, 5, 8, 11, 14, 17]
e, o = count_even_odd(nums)
print("Evens:", e, "Odds:", o)  # Evens: 3 Odds: 3
