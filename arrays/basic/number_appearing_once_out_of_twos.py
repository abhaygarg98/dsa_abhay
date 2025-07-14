def number_appearing_once_out_of_twos(arr):
    xor=0
    for i in range(len(arr)):
        xor = xor^arr[i]

    return xor

arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 9, 9, 8]
print(number_appearing_once_out_of_twos(arr))
