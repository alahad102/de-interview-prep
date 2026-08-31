# iterator
# enumerate, map, zip, chain, reversed

# in order to build a loop
#  save memory
# kafka, flexibility

#iterator is a object. it is a process

# iterable is a thing we can loop over
# string is iterable, int lfoat they are not iterable

letters = ['a', 'b', 'c']
# new_list = []
# for l in letters:
#     new_list.append(l.upper())
#     print(new_list)


# enumerate give value as well as its index number


# for index, value in enumerate(letters):
#     print(index, value)

# reversed

# print(list(reversed(letters)))

# for items in reversed(letters):
#     print(items)

#map iterator

# print(list(map(str.upper, letters)))

numbers = ['1','2','3']
# print(list(map(int, numbers)))

names = [' Maria ', 'John  ', '  kumar']
# print(names)

# print(list(map(str.strip, names)))

# for n in map(str.strip, names):
#     print(n)

# filter

mixed = ['a', 'b', 'c', 10, 13, 'd', 'e', None, False]
print(list(filter(bool, mixed)))

items = ['sql', '123', 'python', '42']

print(list(filter(str.isalpha, items)))

for i in filter(str.isalpha, items):
    print(i)