def find_missing_element(arr):
    n = len(arr) + 1
    expected_sum = n*(n+1)/2
    found_sum = 0
    for i in range(n-1):
        found_sum+=arr[i]
    return expected_sum - found_sum

def find_missing_element_xor(arr):
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0
    for i in range(n-1):
        xor2 = xor2^arr[i]
        xor1 = xor1^(i+1)
    xor1 = xor1^n
    return xor1^xor2

arr = [1, 2, 4, 5]
print(find_missing_element(arr))
print(find_missing_element_xor(arr))
