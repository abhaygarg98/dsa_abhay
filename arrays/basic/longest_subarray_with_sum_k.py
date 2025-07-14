def longest_subarray_with_sum_k_brute(arr, k):
    n = len(arr)
    longest = 0
    s = 0
    for i in range(n):
        for j in range(i,n):
            s+= arr[j]
            if s == k:
                longest = max(j-i+1, longest)
        s = 0
    print(longest)

def longest_subarray_with_sum_k_better(arr, k):
    n = len(arr)
    pre_sums = {}
    s = 0
    longest = 0
    for i in range(n):
        s+=arr[i]
        if s == k:
            longest = max(longest, i+1)
        rem = s - k
        if rem in pre_sums:
            length = i-pre_sums[s-k]
            longest = max(longest, length)
        if s not in pre_sums:
            pre_sums[s] = i
    print(longest)

def longest_subarray_with_sum_k_optimal(arr, k):
    n = len(arr)
    i, j = 0, 0
    longest = 0
    s = arr[i]
    while j < n:
        while s > k and i<=j:
            s-=arr[i]
            i+=1
        if s == k:
            l = j + 1 - i
            longest = max(longest, l)
        j += 1
        if j < n:
            s += arr[j]
    print(longest)




longest_subarray_with_sum_k_brute([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3)
longest_subarray_with_sum_k_better([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3)
longest_subarray_with_sum_k_optimal([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3)