# combining

letters = ['a','b','c']
numbers = [1,2,3]
comb = letters + numbers
print(comb)
print(letters * 2)

comb = [letters, numbers]
print(comb)

numbers.extend(letters)
print(numbers)

# combining using zip. outpt will be list of tuple

letters = ['a','b','c']
numbers = [1,2,3,4]

comb = list(zip(letters, numbers, "786"))
print(comb)