# HackerRank Practice - Nested Lists
#
# You are given the names and grades of several students.
#
# Store each student as:
# [name, grade]
#
# Example:
# students = [
#     ["Harry", 37.21],
#     ["Berry", 37.21],
#     ["Tina", 37.2],
#     ["Akriti", 41],
#     ["Harsh", 39]
# ]
#
# Your task:
#
# 1. Find the lowest DISTINCT grade.
# 2. Find the second lowest DISTINCT grade.
# 3. Find all students who have that second lowest grade.
# 4. If multiple students have the same second lowest grade,
#    sort their names alphabetically.
# 5. Print each name on a separate line.
#
# Example:
#
# Lowest grade:
# 37.2
#
# Second lowest grade:
# 37.21
#
# Students with second lowest grade:
# Berry
# Harry
#
# Important:
# "Second lowest" means the second lowest UNIQUE grade,
# not simply the second item after sorting all grades.


students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
name = []
score = []

for i in students:
    name.append(i[0])
    score.append(i[1])


filter_duplicate = set(score)

distinct_score = sorted(filter_duplicate, reverse=True)

check = distinct_score[-2]

students.sort()

for i in students:
    if (i[1] == check):
        print(i[0])



        

