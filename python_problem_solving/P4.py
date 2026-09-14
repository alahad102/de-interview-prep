# Problem 4 — Word Frequency

# Given:

# words = [
#     "python",
#     "sql",
#     "python",
#     "azure",
#     "sql",
#     "python",
#     "databricks"
# ]

# Create this dictionary:

# {
#     "python": 3,
#     "sql": 2,
#     "azure": 1,
#     "databricks": 1
# }

# Don't use Counter yet. Build the dictionary yourself.


# words = [
#     "python",
#     "sql",
#     "python",
#     "azure",
#     "sql",
#     "python",
#     "databricks"
# ]


# words_dictionary = {}

# for w in words:
#     words_dictionary[w] = words.count(w)

# print(words_dictionary)

words = [
    "python",
    "sql",
    "python",
    "azure",
    "sql",
    "python",
    "databricks"
]

words_dictionary = {}

for w in words:
    if w in words_dictionary:
        words_dictionary[w] += 1
    else:
        words_dictionary[w] = 1

print(words_dictionary)


