# user defined function

def my_function():
    print("my function is working")

# my_function()
# print(type(my_function))

#built in function
# print(len("python"))

#function from libraray
import math
number = 4.2
# print(math.floor(number))

def pow_fun(x):
    x = x ** 2
    return x

# print(pow_fun(5))

# postional arguement 

def my_func(x,y):
    print(x*2)
    print(y*2)

# my_func(5,3) #postional arguements
# my_func(y = 3, x =5) #keyword arguements

#mixed arguements
# my_func(5, y=3) #but must start with positional arguments


#default parameter

def my_func_2(x,y,z = 1): # default value will be processed if dont mention in function call
    print(x+y+z)

# my_func_2(5,4,5)

# *args **kwarge

def total(*args):
    print(sum(args))

# total(1,2)

# total(1,2,3,4,5,6,7)

def create_user(**kwargs):
    print(kwargs)


create_user(id = 1, name = 'Ahad')


# transforamtion function with return

def clean_and_split_email(email):
    cl_email = email.strip().lower()
    # sara@gmail.com
    username, domain = cl_email.split("@")
    return {"username:": username, "domain": domain}

my_info = clean_and_split_email("    alaHAD102@gmail.com   ")
print(my_info)