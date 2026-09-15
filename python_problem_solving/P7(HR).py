# HackerRank Practice - Find the Runner-Up Score
#
# You are given a list of participant scores from a university
# sports competition.
#
# Your task is to find and print the runner-up score.
#
# The runner-up score means:
#
# The second highest DISTINCT score.
#
# If the highest score appears multiple times, those duplicate
# highest scores should not be considered separately.
#
#
# Example:
#
# scores = [2, 3, 6, 6, 5]
#
# Highest score:
# 6
#
# After ignoring the duplicate 6, the next highest score is:
# 5
#
# Therefore:
#
# Runner-up score = 5
#
#
# Input:
#
# First line:
# Number of scores, n
#
# Second line:
# n integer scores separated by spaces
#
#
# Sample Input:
#
# 5
# 2 3 6 6 5
#
#
# Expected Output:
#
# 5
#
#
# Goal:
# Find the second highest DISTINCT value in the list.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

final_list = list(arr)

new_list = []

for item in final_list:
    if item not in new_list:
        new_list.append(item)

new_list.sort()
print(new_list[-2])