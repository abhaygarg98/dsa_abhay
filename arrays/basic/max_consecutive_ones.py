def maximum_consecutive_ones(arr):
    max_count = 0
    counter = 0
    for i in range(len(arr)):
        if arr[i]==1:
            counter+=1
        else:
            if counter > max_count:
                max_count = counter
            counter = 0
    return max_count

# arr = [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]
arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print(maximum_consecutive_ones(arr))
