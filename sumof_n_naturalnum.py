n = int(input("Enter a non-negative integer n: "))
if n < 0:
    raise ValueError("n must be non-negative")
total = n * (n + 1) // 2
print("Sum of first", n, "natural numbers =", total)
