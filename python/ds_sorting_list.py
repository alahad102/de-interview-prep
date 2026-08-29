# how to order data in list

numbers = [2,3,5,6,1,4]
numbers.sort()
print(numbers)

letters = ['c','a','b']
# letters.sort()
# print(letters)
letters.sort(reverse = True)
print(letters)

matrix = [
    ['x','e','f'],
    ['a','h','i'],
    ['a','b','c']
]

matrix[0].sort()
print(matrix)

new_matrix = sorted(matrix)
print(new_matrix)

# reversing list. no sorting logic

new_matrix.reverse()
print(new_matrix)

reverse_matrix = reversed(new_matrix)
print(reverse_matrix)