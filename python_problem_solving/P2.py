# Problem 2 — Find the Largest Without max()

# Given:

# numbers = [17, 4, 29, 8, 13, 41, 6]

# Find the largest number without using:

# max()
# sorted()
# sort()

# Expected:

# Largest number: 41

numbers = [17, 4, 29, 8, 13, 41, 6]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
print("Largest number:", largest)


