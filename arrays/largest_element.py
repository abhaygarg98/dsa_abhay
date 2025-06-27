def largest_element(arr):
    maximum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

print(largest_element([1, 0, 9, 100, 8]))