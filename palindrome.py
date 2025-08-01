n = int(input("Enter a number: "))
original_num = n
rev = 0
while(n > 0):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original_num == rev:
    print(original_num,"is a palindrome number")
else:
    print(original_num,"is not a palindrome number")