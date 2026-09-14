# Problem 1 — Even/Odd Statistics

# Given:

# numbers = [12, 7, 5, 20, 18, 3, 11, 6]

# Write Python code that prints:

# Even numbers: 4
# Odd numbers: 4
# Sum of even numbers: 56
# Sum of odd numbers: 26

numbers = [12, 7, 5, 20, 18, 3, 11, 6]

e_count = 0
o_count = 0
e_sum = 0
o_sum = 0

for n in numbers:
    if(n % 2 == 0):
        e_count = e_count + 1
        e_sum = e_sum + n
    else:
        o_count = o_count + 1
        o_sum = o_sum + n

print("Even numbers:", e_count)
print("Odd numbers:", o_count)
print("Sum of Even numbers:", e_sum)
print("Sum of Odd numbers:", o_sum)