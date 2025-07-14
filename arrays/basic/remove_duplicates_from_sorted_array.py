def remove_duplicates_from_sorted_array(arr):
    i = 0
    j = i + 1
    while j < len(arr):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
        j+=1
    return i+1

print(remove_duplicates_from_sorted_array([-2, 2, 4, 4, 4, 4, 5, 5]))