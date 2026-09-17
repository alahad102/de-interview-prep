def average(array):
    my_set = set(array)
    return sum(my_set) / len(my_set)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)