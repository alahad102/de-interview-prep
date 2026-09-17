# HackerRank Practice - Finding the Percentage
#
# You are given records for several students.
# Each student has:
# - a name
# - a list of marks
#
# Store the data in a dictionary in this form:
#
# {
#     "Krishna": [67, 68, 69],
#     "Arjun": [70, 98, 63],
#     "Malika": [52, 56, 60]
# }
#
# After reading all student records, you are given a student name
# called query_name.
#
# Your task:
# 1. Find that student's marks from the dictionary.
# 2. Calculate the average of the marks.
# 3. Print the average with exactly 2 decimal places.
#
# Example:
#
# Marks for Malika:
# [52, 56, 60]
#
# Average:
# (52 + 56 + 60) / 3 = 56
#
# Expected output:
# 56.00

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for k,v in student_marks.items():
        if k == query_name:
            average = sum(v) / len(v)
            print(f"{average:.2f}")