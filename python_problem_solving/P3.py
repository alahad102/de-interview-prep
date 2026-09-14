# Problem 3 — Clean Customer Names

# You receive:

# customers = [
#     "  JOHN SMITH ",
#     "alice brown",
#     "  Bob Johnson",
#     "MARY WILLIAMS  "
# ]

# Produce:

# ["John Smith", "Alice Brown", "Bob Johnson", "Mary Williams"]

# This is particularly relevant to Data Engineering because you're effectively performing a small data-cleaning transformation.

customers = [
    "  JOHN SMITH ",
    "alice brown",
    "  Bob Johnson",
    "MARY WILLIAMS  "
]

clean_customer = []

for c in customers:
    clean = c.strip().title()
    clean_customer.append(clean)

print(clean_customer)