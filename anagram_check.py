def is_anagram(a, b):
    a = sorted(c for c in a.lower() if c.isalnum())
    b = sorted(c for c in b.lower() if c.isalnum())
    return a == b

# quick tests
print(is_anagram("Listen", "Silent"))            # True
print(is_anagram("Dormitory", "Dirty room!!"))   # True
print(is_anagram("Hello", "Olelhh"))             # False
