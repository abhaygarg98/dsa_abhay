def majority_element_greater_than_half_length_better(arr):
    dict =  {}
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]]+=1
        else:
            dict[arr[i]] = 1
    max_val = 0
    max_key = -1
    for key, value in dict.items():
        if value > max_val and value > len(arr)/2:
            max_val = value
            max_key = key

    print(max_key)

# Moore's Voting algorithm
def majority_element_greater_than_half_length_optimal(arr):
    el = None
    count = 0
    inc = 0
    for i in range(len(arr)):
        if count == 0:
            el = arr[i]
            count=1
        elif arr[i] == el:
            count+=1
        else:
            count-=1
    if count != 0:
        for i in range(0, len(arr)):
            if arr[i] == el:
                inc+=1
    if inc > len(arr)/2:
        print(el)
    else:
        print(-1)



arr = [2, 2, 3, 3, 1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2]
majority_element_greater_than_half_length_better(arr)
majority_element_greater_than_half_length_optimal(arr)