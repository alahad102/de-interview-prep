# list allow duplicates, ordered , indexed, mutatable

my_list = [10,20,30,10]
# print(my_list) # allow duplicates

my_list = [5,4,8,6,8]
# print(my_list) # ordered so dont change postion

# print(my_list[0]) # indexed means i can access through index

my_list[0] = 500
# print(my_list) #mutable we can update value

# tuples

my_tuple = (5,8,9,5)
# print(my_tuple) # allow duplicates #also ordered
# print(my_tuple[-2]) # indexed. i can access through index

# my_tuple[0] = 50
#print(my_tuple) #error because not mutable


my_set = {5,8,6,9,5}
# print(my_set) # done allow duplicates and not ordered

# print(my_set[0]) # error because not indexed

my_set.remove(5) #so set mutable
# print(my_set)

my_dic = { 1:'a', 2:'b', 3:'c', 2:'x'}
# print(my_dic) #ordered #dont allow duplcates key and vlaue both need to be unique

# print(my_dic[1]) # not indexed, key is the index

my_dic[1] = 'xyz'
# print(my_dic) # mutable using key


#set method

my_set = {10,20,30,40}

my_set.add(10)
print(my_set)

my_set.update("hi")
my_set.update({2,3})
my_set |= {5,6}
my_set.discard(500)
print(my_set)

# different operator in set
A = {1,2,3}
B = {1,3}
print(A.union(B))
print(A | B)
print(A.intersection(B))
print(A.difference(B))
print(A - B)
print(B.difference(A))
print(B - A)

print(A.symmetric_difference(B))
print(A ^ B)

print(A.issubset(B))
print(B.issubset(A))
print(A.issuperset(B))
print(A.isdisjoint(B))