# HackerRank Practice - Introduction to Sets
#
# You are given a list of plant heights.
#
# Some heights may appear more than once.
#
# Your task:
# 1. Remove duplicate heights.
# 2. Keep only the distinct heights.
# 3. Calculate the average of those distinct heights.
# 4. Return the average as a float.
#
# Formula:
#
# average = sum of distinct heights / number of distinct heights
#
# Example:
#
# arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
#
# Distinct heights:
# {161, 182, 154, 176, 170, 167, 171, 174}
#
# Expected result:
# 169.375
#
# Goal:
# Use a set to eliminate duplicate values.

def average(array):
    my_set = set(array)
    return sum(my_set) / len(my_set)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)