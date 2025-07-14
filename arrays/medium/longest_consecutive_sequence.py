import sys


def longest_consecutive_sequence_brute(arr):
    longest = 0
    n = len(arr)

    for i in range(n):
        current = arr[i]
        count = 1

        while current + 1 in arr:
            current += 1
            count += 1

        longest = max(longest, count)

    print(longest)

def longest_consecutive_sequence_better(arr):
    arr = list(sorted(arr))
    lowest = -sys.maxsize
    counter = 1
    longest = 1
    for i in range(len(arr)):
        if arr[i] == lowest + 1:
            counter+=1
            lowest+=1
        elif arr[i] == lowest:
            continue
        else:
            longest = max(longest, counter)
            counter = 1
            lowest = arr[i]
    print(longest)

def longest_consecutive_sequence_optimal(arr):
    arr_set = set(arr)
    longest = 0
    for item in arr_set:
        if item-1 not in arr_set:
            current = item
            counter = 1
            while item+1 in arr_set:
                item+=1
                counter+=1
            longest = max(longest, counter)
    print(longest)




longest_consecutive_sequence_brute([102, 3, 3, 4, 101, 100, 1, 1, 2, 2])
longest_consecutive_sequence_better([100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2, 5, 7])
longest_consecutive_sequence_optimal([100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2, 5, 7])