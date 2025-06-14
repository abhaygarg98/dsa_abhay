def qs(arr, low, high):
    if low < high:
        p_index = get_pivot_index(arr, low, high)
        qs(arr, low, p_index-1)
        qs(arr, p_index + 1, high)

def get_pivot_index(arr, low, high) -> int:
    pivot = low
    i, j = low, high
    while i < j:
        while arr[i] <= arr[pivot] and i < high:
            i+=1
        while arr[j] > arr[pivot] and j > low:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j

# arr1 = [4, 3, 1, 6, 2, 8, 9]
arr1 = [4, 6, 2, 5, 7, 9, 1, 3]
qs(arr1, 0, len(arr1)-1)
print(arr1)

# time complexity: O(nlog(n))
# space complexity: O(1)
