# remove every item

numbers = [1,2,3,4]
numbers.clear()
print(numbers)

# removing specific item by value. it will remove first found
numbers = [1,2,3,2]
numbers.remove(2)
print(numbers)

# remove specific value by index
numbers = [1,2,3]
print(numbers.pop())
print(numbers)

numbers = [1,2,3]
print(numbers.pop(1))
print(numbers)

# matrix

matrix = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]

print(matrix.remove(['a','b','c']))
print(matrix)

matrix = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]

print(matrix[0].pop(1))
print(matrix)
