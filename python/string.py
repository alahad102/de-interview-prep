# built in function
# type & str

name = "Ahad"
# print(type(name))

age = 30
# print(type(age))
# print("your age is:" + str(age))

age = age + 5
# print(age)

age = str(age)
# print(type(age))

# math function
# len() & count()

password = '123a'
# print(len(password))

text = """"
python is easy to learn.
python is powerful.
Python is popular.
"""

# print(text.count("python"))

# transformation
# replace() function

# print(text.replace('Python', 'C++'))

phone = '214-425-5648'
# print(phone.replace('-', ''))

price = "$1,299.99"
# print(price.replace("$", '').replace(",", ""))

# challenge

phone2 = "+49 (176) 123-4567"

# print(phone2.replace("+","").replace("(", "").replace(")","").replace("-","").replace(" ", ""))

# transformation

first_name = "ahad"
last_name = "khan"
last_name = first_name + " " + last_name
# print(last_name)

folder = "C:/users/ahad/"
file = "report.csv"
full_file_path = folder + file
# print(full_file_path)

# f-string
name = 'ahad'
age = 34
is_student = False
# print("my name is " + name + " I am " + str(age) + " years old, and student status is " + str(is_student) + ".")

# print(f"my name is {name}, i am {age} years old, and student status is {is_student}")

# f-string can process expression as well

# print(f" 2 + 3 = {2 + 3}")

# print(f"{{this is me}}")

# data transformation
# split()

text = "Ahad-30-USA"

text1 = text.split('-')

# print(text1)
# print(type(text1))

stamp = "2026-09-20 14:30"
# print(stamp.split(" "))

csv_file = "1234,Max,USA,76706,M"
# print(csv_file.split(","))