import math

num = int(input("Enter a number: "))
if num > 1:
    print("Factorial of ",num,"is ",math.factorial(num))
else:
    print("Factorial is not defined for a negative number")