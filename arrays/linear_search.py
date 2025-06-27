def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i

    return -1


print(linear_search([4, 7, 2, -1, 6, 3, 7, 8, 3, 7], 3))