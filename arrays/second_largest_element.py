def second_largest_element(arr):
    if len(arr) < 2:
        return None
    maximum, second_max = arr[0], float('-inf')
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            second_max = maximum
            maximum = arr[i]
        elif second_max < arr[i] < maximum:
            second_max = arr[i]

    return second_max

print(second_largest_element([-10, -20, -5, -15]))