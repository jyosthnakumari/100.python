import string

def remove_punct(s):
    table = str.maketrans('', '', string.punctuation)
    return s.translate(table)

print(remove_punct("Hello, world!! How's it going?"))
# Output: Hello world Hows it going
