import sys

def maximum_subarray_sum_better(arr):
    n = len(arr)
    maximum=-sys.maxsize - 1
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            maximum = max(maximum, s)

    print(maximum)

#Kadane's algorithm
def maximum_subarray_sum_optimal(arr):
    n = len(arr)
    maximum = -sys.maxsize - 1
    s = 0
    start_ind, end_ind = -1, -1
    for i in range(n):
        if s == 0:
            start_ind = i
        s+=arr[i]
        maximum = max(s, maximum)
        if maximum == s:
            end_ind = i
        if s < 0:
            s = 0
    print(f'{arr[start_ind:end_ind+1]} - maximum: {maximum}')

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
arr1 = [-4, -3, -2, -1]
maximum_subarray_sum_better(arr)
maximum_subarray_sum_optimal(arr)