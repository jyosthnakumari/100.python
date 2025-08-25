sentence = "I love learning data science with Python"
words = sentence.split()
print(max(words, key=len))   # Output: science
