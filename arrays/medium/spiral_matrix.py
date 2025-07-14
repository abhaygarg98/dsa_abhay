def spiral_matrix(arr):
    n = len(arr)
    m = len(arr[0])
    top, left = 0, 0
    right = m-1
    bottom = n-1
    while left<=right and top<=bottom:
        for i in range(left, right+1):
            print(arr[top][i])
        top+=1
        for i in range(top, bottom+1):
            print(arr[i][right])
        right-=1
        if top<=bottom:
            for i in range(right, left-1, -1):
                print(arr[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom, top-1, -1):
                print(arr[i][left])
            left+=1


matrix = [[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8], [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10], [10, 15, 14, 13, 12, 11]]
# matrix = [[1, 2, 3, 4, 5, 6]]
# matrix = [[1, 2, 3, 4, 5, 6], [12, 11, 10, 9, 8, 7]]
# matrix = [[1], [2], [3], [4], [5], [6]]
# matrix = [[1, 2], [12, 3], [11, 4], [10, 5], [9, 6], [8, 7]]
# matrix = [[1]]
spiral_matrix(matrix)