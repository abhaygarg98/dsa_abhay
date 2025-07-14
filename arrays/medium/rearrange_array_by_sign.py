def rearrange_array_by_sign_brute(arr):
    pos_arr = []
    neg_arr = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            pos_arr.append(arr[i])
        else:
            neg_arr.append(arr[i])
    for i in range(int(len(arr)/2)):
        arr[2*i] = pos_arr[i]
        arr[2*i+1] = neg_arr[i]
    print(arr)

def rearrange_array_by_sign_optimal(arr):
    pos_ind = 0
    neg_ind = 1
    ans_arr = [0]*len(arr)
    for i in range(len(arr)):
        if arr[i] >= 0:
            ans_arr[pos_ind] = arr[i]
            pos_ind+=2
        else:
            ans_arr[neg_ind] = arr[i]
            neg_ind+=2
    print(ans_arr)

def rearrange_uneven_array_by_sign(arr):
    n = len(arr)
    pos_arr = []
    neg_arr = []
    for i in range(n):
        if arr[i] >= 0:
            pos_arr.append(arr[i])
        else:
            neg_arr.append(arr[i])
    if len(pos_arr) > len(neg_arr):
        for i in range(len(neg_arr)):
            arr[2*i] = pos_arr[i]
            arr[2*i + 1] = neg_arr[i]
        for j in range(len(neg_arr), len(pos_arr)):
            arr[len(neg_arr) + j] = pos_arr[j]
    else:
        for i in range(len(pos_arr)):
            arr[2 * i] = pos_arr[i]
            arr[2 * i + 1] = neg_arr[i]
        for j in range(len(pos_arr), len(neg_arr)):
            arr[len(pos_arr) + j] = neg_arr[j]
    print(arr)


rearrange_array_by_sign_brute([-2, 5, 7, 0, -3, -6, -5, 1, 8, -1])
rearrange_array_by_sign_optimal([-2, 5, 7, 0, -3, -6, -5, 1, 8, -1])
rearrange_uneven_array_by_sign([-2, 5, 7, -5, 6, 9, 12, 9, 0, -3, -6, -5, 1, 8, -1])