def sort_array_of_0_1_2_s_better(arr):
    count_0, count_1, count_2 = 0, 0, 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count_0+=1
        elif arr[i] == 1:
            count_1+=1
        else: count_2+=1

    arr = [0]*count_0 + [1]*count_1 + [2]*count_2
    print(arr)


#Dutch National Flag Algorithm
def sort_array_of_0_1_2_s_optimal(arr):
    n = len(arr)
    low, mid = 0, 0
    high = n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
        else:
            mid+=1
    print(arr)


arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort_array_of_0_1_2_s_better(arr)
sort_array_of_0_1_2_s_optimal(arr)