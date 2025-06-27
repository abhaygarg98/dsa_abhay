def move_all_zeroes_to_end(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break

    for i in range(j+1, len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1

    return arr







print(move_all_zeroes_to_end([0, 5, 0, 6, 3, 0, 0, 0, 1, 0, 9, 0]))