x = int(input("Enter an number: "))

if x>1:
    for i in range (2, int(0.5**x)+1):
        if x % 2 == 0:
            print(x,"is not a prime number")
        break
    else:
        print(x,"is a prime number")
else:
    print(x,"is not a prime number")