def is_pangram(s):
    import string
    return set(string.ascii_lowercase) <= set(ch for ch in s.lower() if ch.isalpha())

# quick tests
print(is_pangram("The quick brown fox jumps over a lazy dog"))  # True
print(is_pangram("Sphinx of black quartz, judge my vow"))       # True
print(is_pangram("Hello world"))                                 # False
