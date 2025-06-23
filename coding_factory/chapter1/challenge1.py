"""
Prints each character of the word 'Factory' incrementally repeated on  each line:
"""

word = "Factory"

for i in range(len(word)):
    print(f"{word[i]}" * (i + 1))