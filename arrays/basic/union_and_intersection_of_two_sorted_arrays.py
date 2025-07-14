
def union_of_two_sorted_arrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i, j = 0, 0
    union_arr = []
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i+=1
        else:
            if len(union_arr) == 0 or union_arr[-1] != arr2[j]:
                union_arr.append(arr2[j])
            j+=1
    while j < m:
        if len(union_arr) == 0 or union_arr[-1] != arr2[j]:
            union_arr.append(arr2[j])
        j += 1
    while i < n:
        if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
            union_arr.append(arr1[i])
        i += 1
    return union_arr

def intersection_of_two_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i+=1
        elif arr1[i] == arr2[j]:
            ans.append(arr1[i])
            i+=1
            j+=1
        else:
            j+=1
    return ans



arr1 = [1, 1, 2, 2, 3]
arr2 = [2, 2, 3, 3]

print(union_of_two_sorted_arrays(arr1, arr2))
print(intersection_of_two_sorted_arrays(arr1, arr2))
