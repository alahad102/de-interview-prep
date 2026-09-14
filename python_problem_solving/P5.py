# Day 1 - Final Challenge: Most Frequent Valid Customer
#
# Given the customer list below:
#
# customers = [
#     "  Alice ",
#     "bob",
#     "ALICE",
#     "",
#     " Bob ",
#     "charlie",
#     "alice",
#     "   ",
#     "CHARLIE",
#     "alice"
# ]
#
# Tasks:
# 1. Remove leading and trailing spaces from each name.
# 2. Ignore empty names after cleaning.
# 3. Treat names case-insensitively.
# 4. Count how many times each customer appears.
# 5. Find the customer who appears most frequently.
# 6. Print the frequency dictionary, the most frequent customer,
#    and their frequency.
#
# Do NOT use:
# - collections.Counter
# - max()
# - .count()

customers = [
    "  Alice ",
    "bob",
    "ALICE",
    "",
    " Bob ",
    "charlie",
    "alice",
    "   ",
    "CHARLIE",
    "alice"
]

frequency = {}

for customer in customers:
    customer = customer.strip().lower()

    if customer == "":
        continue

    if customer in frequency:
        frequency[customer] += 1
    else:
        frequency[customer] = 1

most_frequent_customer = None
highest_frequency = 0

for customer, count in frequency.items():
    if count > highest_frequency:
        highest_frequency = count
        most_frequent_customer = customer

print(frequency)
print("Most frequent customer:", most_frequent_customer)
print("Frequency:", highest_frequency)

    