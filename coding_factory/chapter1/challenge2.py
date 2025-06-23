"""
Prints each character of the word 'Factory' incrementally repeated, followed by a decreasing number of asterisks
to form a right alighned triangle
"""

word = "Factory"

# first solution
for i in range(len(word)):
    print(f"{word[i]}" * (i + 1), "*" * (len(word) - (i + 1)), sep="")

print()


# cleaner solution
for i in range(len(word)):
    print(f"{word[i] * (i + 1):*<{len(word)}}")

print()


# more modular solution
for i in range(len(word)):
    char = word[i]
    repeat_count = i + 1
    total_width = len(word)
    formatted = f"{char * repeat_count:*<{total_width}}"
    
    print(formatted)
