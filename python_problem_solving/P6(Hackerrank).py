# HackerRank Practice - List Comprehensions
#
# You are given four integers:
# x, y, z, and n.
#
# x, y, and z represent the maximum coordinates of a 3D grid.
#
# Generate every possible coordinate in the form:
#
# [i, j, k]
#
# where:
# 0 <= i <= x
# 0 <= j <= y
# 0 <= k <= z
#
# However, exclude any coordinate where:
#
# i + j + k == n
#
# Print all remaining coordinates as a list.
#
# Use a LIST COMPREHENSION instead of writing multiple nested
# for loops.
#
# The coordinates should appear in lexicographic increasing order.
#
#
# Example:
#
# Input:
# x = 1
# y = 1
# z = 1
# n = 2
#
# Possible coordinates include:
# [0, 0, 0]
# [0, 0, 1]
# [0, 1, 0]
# [0, 1, 1]
# [1, 0, 0]
# [1, 0, 1]
# [1, 1, 0]
# [1, 1, 1]
#
# Remove coordinates whose values sum to 2.
#
# Expected output:
#
# [[0, 0, 0],
#  [0, 0, 1],
#  [0, 1, 0],
#  [1, 0, 0],
#  [1, 1, 1]]
#
#
# Goal:
# Solve the problem using ONE list comprehension.

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if(i + j + k != n):
#                 print(f"{i},{j},{k}")

final_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(final_list)

            