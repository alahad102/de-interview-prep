# copy list
# in this way it just making a new reference. 
# so whatever change will be in list2 it will reflect in list1

list1 = [1,2,3]
list2 = list1
# print(list1)
# print(list2)
list2.append(4)
# print(list1)
# print(list2)

# shallow copy
letters = ['a','b','c']
letters_copy = letters.copy()
# print("orignal:", letters)
# print("copy:", letters_copy)

letters_copy.append('d')
letters.pop()

# print("orignal:", letters)
# print("copy:", letters_copy)

matrix = [
    [1,2,3],
    [4,5,6]
]

matrix_copy = matrix.copy()

# print(matrix)
# print(matrix_copy)

matrix.pop()
matrix_copy[0].append(10)

# print(matrix)
# print(matrix_copy)

#deep copy by importing copy module

import copy

matrix = [
    [1,2,3],
    [4,5,6]
]

matrix_copy = copy.deepcopy(matrix)

matrix.pop()
matrix_copy[0].append(10)

print(matrix)
print(matrix_copy)



