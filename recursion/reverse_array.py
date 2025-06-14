class Solution:

    def __init__(self):
        self.reversedArray = []
    
    def reverse(self, arr, n):
        if n == 0:
            return self.reversedArray
        self.reversedArray.append(arr[n-1])
        return self.reverse(arr, n-1)

sol1 = Solution()
sol2 = Solution()
print(sol1.reverse([1,2,3,4,5], 5))
print(sol2.reverse([1,2,1,1,5,1], 6))