# while loop

# "i = 1
# while i < 5:
#     print(i)
#     i= i+1"

# while condition. type 1
# while true, type 2

# answer = ""
# while answer != "yes":
#     answer = input("do u agree? (yes/no): ")
# print("thank you")

#while true with break
# i = 1
# while True:
#     print(i)
#     if(i == 5):  
#         break
#     i = i+1

# while True:
#     answer = input("Do you agree?(yes/no): ")
#     if answer == "yes":
#         print("correct answer")
#         break
# print("thank you")

# challenge problem

i = 0
while True:
    answer = input("enter your answer(yes/no): ")
    i = i +1
    if (answer == 'yes'):
        print("glad we are in the same page")
        break
    if (i == 3):
        print("3 strikes, you are out")
        break
print("thank you")

