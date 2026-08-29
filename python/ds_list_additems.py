# append() which will add value at the last
numbers = [1,2,3,4]
numbers.append(5)
print(numbers)

letter = ['a','b','c']
letter.append('x')
print(letter)

#add value in specific position

letter.insert(1,'y')
print(letter)
letter.insert(0,'M')
print(letter)

matrix = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]
print(matrix)
matrix.append(['x','y','z'])
print(matrix)
matrix.insert(0, ['a','a','a'])
print(matrix)

matrix[1].append('x')
print(matrix)