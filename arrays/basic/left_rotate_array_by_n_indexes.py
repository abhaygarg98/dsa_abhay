
# def left_rotate_by_n_indexes(arr, n):
#     m = len(arr)
#     if n < 0:
#         return
#     if n in [m, 0]:
#         return arr
#     n = n%m
#     temp_arr = arr[:n]
#     for i in range(n,m):
#         arr[i-n] = arr[i]
#     arr[m-n:] = temp_arr
#     return arr
#
# # TC: O(m+n)
# # SC: O(n)

def left_rotate_by_n_indexes(arr, n):
    m = len(arr)
    if n<0 or n in [0,m]:
        return arr
    n = n % m
    return arr[n:] + arr[:n]

# TC: O(2m)
# SC: O(1)


print(left_rotate_by_n_indexes([6, 2, 1, 8, 9, -4], 103))
