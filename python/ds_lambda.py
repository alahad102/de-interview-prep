# lambda
# own custom logic
# anonymous function

multiply = lambda x: x * 2
print(multiply(6))

addition = lambda x,y: x + y
print(addition(5,2))

check = lambda i: i in "python"
print(check('x'))

# lambda + map

prices = ['$12.50', '$9.99','$100.00']


x = lambda p: float(p.replace('$', ''))

print(list(map(x, prices)))

# lambda + filter

prices = [120, 30,300,80]

print(list(filter(lambda p: p >= 100, prices)))

students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]
print(list(filter(lambda row: row[1] > 70, students)))

print(list(filter(lambda row: row[0].startswith('M'), students)))


