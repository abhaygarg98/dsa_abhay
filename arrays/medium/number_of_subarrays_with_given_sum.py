def number_of_subarrays_with_given_sum_brute(arr, k):
    count = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s+=arr[j]
            if s == k:
                count+=1
    print(count)

#prefix sum algorithm
def number_of_subarrays_with_given_sum_optimal(arr, k):
    count = 0
    dict = {0:1}
    pre_sum = 0
    for i in range(len(arr)):
        pre_sum+=arr[i]
        rem = pre_sum-k
        if rem in dict.keys():
            count += dict[rem]
        if pre_sum not in dict.keys():
            dict[pre_sum] = 1
        else:
            dict[pre_sum]+=1

    print(count, dict)


arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k = 3
number_of_subarrays_with_given_sum_brute(arr, k)
number_of_subarrays_with_given_sum_optimal(arr, k)