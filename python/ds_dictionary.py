my_dict = {
    'a':10,
    'b':20,
    'c':20,
    'a':50
}
print(my_dict) #so it is ordered #keys are unique, value allow duplicate

print(my_dict['b']) #not indexed. need key to access

my_dict['c'] = 6000
print(my_dict) # dictionary is mutable

# dic method
user ={"id":1, "age": 30, "city":"berlin"}

print(user.get("age")) # get doesnot break code even if the key doesnt exist
print(user.get("name", "unknown"))

#checks
print("age" in user)
print("name" not in user)

#view object

print(user.keys()) #getting key values only
print(user.values()) #getting value only
print(user.items())
print(user)

for u in user:
    print(u,user[u])

for key, value in user.items():
    print(key, value)

user1 = {
    "id": 1,
    "name": "John",
    "age": 30,
    "city": "Berlin"
}

user2 = {}

for key, value in user1.items():
    if isinstance(value, str):
        user2[key.upper()] = value.upper()
print(user2)
    

user3 = {
    k: v.upper()
    for k,v in user1.items()
    if isinstance(v, str)
}
print(user3)


    
