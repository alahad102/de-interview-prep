# indexing & slicing

lst = ['a','b','c','d']
# print(lst[0])
# print(lst[-1])
# print(lst[0:2])
# print(lst[:2])

matrix_list =[list(range(5)),
              list(range(5,10)),
              list(range(10,15))]
# print(matrix_list)
# print(matrix_list[2][0:2])
# print(matrix_list[0][0])


# unpacking list

letter = list("Python")
# print(letter)

# for item in letter:
#     print(item)

person = ['Maria', 29, 'data engineer', 'spain']

# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]
# print(f"name = {name}\nage = {age}")

# name , age, role, country = person
# print(name)
# print(country)

# rest collector *

# name , country = person[0], person[-1]
# print(name)
# print(country)

name, *details, country = person
# print(name)
# print(details)
# print(country)

numbers = [1,2]
first , second, *rest = numbers
# print(first)
# print(rest)

# skipping item using underscore _

lst = ['maria','30', 'spain', 'data engineer']
name, _, country, _ = lst
# print(name)
# print(_)

# underscore and asterix together

lst = list(range(10))
# print(lst)

first, *_, last= lst
print(first)
print(_)
