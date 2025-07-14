def find_two_sum_indexes_brute(arr, target):
    n = len(arr)
    found_indexes = []
    for i in range(n-1):
        for j in range(i, n):
            if arr[i] + arr[j] == target:
                found_indexes.append([i,j])
    if not found_indexes:
        print([-1, -1])
    else:
        print(found_indexes)



def find_two_sum_indexes_better(arr, target):
    n = len(arr)
    els = {}
    found_indexes = []
    for i in range(n):
        rem = target - arr[i]
        if rem in els:
            found_indexes.append([els[rem], i])
        else:
            els[arr[i]] = i
    if not found_indexes:
        print([-1, -1])
    else:
        print(found_indexes)

find_two_sum_indexes_brute([2, 6, 5, 8, 11], 15)
find_two_sum_indexes_better([2, 6, 5, 8, 11], 14)