def rotate_matrix_by_90_deg_brute(arr, n):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[j][n-1-i] = arr[i][j]
    print(ans)

def rotate_matrix_by_90_deg_better(arr, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if i!=j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for i in range(n):
        arr[i] = list(reversed(arr[i]))
    print(arr)

matrix = [
    [6, 4, 3, 2],
    [1, 1, 6, 4],
    [8, 9, 0, 1],
    [2, 3, 8, 2]
]
rotate_matrix_by_90_deg_brute(matrix, 4)
rotate_matrix_by_90_deg_better(matrix, 4)
