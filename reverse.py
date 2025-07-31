number = int(input("Enter a number: "))

rev = 0
while(number > 0):
    digit = number % 10
    rev = rev * 10 + digit
    number = number//10

print("Reverse of the given number is : ",rev)