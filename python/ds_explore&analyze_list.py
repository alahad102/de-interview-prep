numbers = [1,5,5,2,4,3]
print("MAX:", max(numbers))
print("MIN:", min(numbers))
print("Sum:", sum(numbers))
print("length:", len(numbers))

print("ALL:", all(numbers))
print("ALL:", all([1, 0, 2]))
print("ALL:", all(['a', '', 'b']))
print("ALL:", all(['a','b','c']))

print("Any:", any(numbers))
print("Any:", any([14,0,0]))
print("Any:", any([0,0,0]))

#count and index method
#index only return first occurance

print("Count:", numbers.count(5))
print("index:", numbers.index(5))

#in operator
print(4 in numbers)
print(40 in numbers)
print(40 not in numbers)

