def leaders_in_array_brute(arr):
    leaders = []
    for i in range(len(arr) - 1):
        leader = True
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader:
            leaders.append(arr[i])
    print(leaders)

def leaders_in_array_optimal(arr):
    maximum = arr[-1]
    leaders = []
    for i in range(len(arr)-2, 0, -1):
        if arr[i] > maximum:
            maximum = arr[i]
            leaders.append(arr[i])
    print(leaders)


leaders_in_array_brute([10, 22, 12, 3, 0, 6])
leaders_in_array_optimal([10, 22, 12, 3, 0, 6])