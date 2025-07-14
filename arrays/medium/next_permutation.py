def next_permutation(arr):
    n = len(arr)
    index = -1
    for i in range(n-2, 0, -1):
        if arr[i+1] > arr[i]:
            index = i
            break
    if index!=-1:
        for i in range(n-1, 0, -1):
            if arr[i] > arr[index]:
                arr[i], arr[index] = arr[index], arr[i]
                break
    arr[index+1:n] = arr[index+1:n][::-1]
    print(arr)

next_permutation([2, 1, 5, 4, 3, 0, 0])
next_permutation([5, 4, 3, 2, 1, 0, 0])