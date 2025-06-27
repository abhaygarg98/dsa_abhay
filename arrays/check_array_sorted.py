def check_array_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            return False
    return True

print(check_array_sorted([4, 6, 9, 10, 50, 50, 49]))