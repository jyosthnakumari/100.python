n = int(input("Enter an integer: "))

print("Binary (with prefix):", bin(n))      # e.g. 13 -> '0b1101'
print("Octal  (with prefix):", oct(n))      # e.g. 13 -> '0o15'
print("Hex    (with prefix):", hex(n))      # e.g. 13 -> '0xd'

# Without prefixes:
print("Binary (no prefix):", format(n, 'b'))   # '1101'
print("Octal  (no prefix):", format(n, 'o'))   # '15'
print("Hex    (no prefix):", format(n, 'x'))   # 'd'  (use 'X' for uppercase)
