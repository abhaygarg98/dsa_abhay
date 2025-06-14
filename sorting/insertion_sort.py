class InsertionSort:

    def sort(self, arr):
        n = len(arr)
        did_swap = False
        for i in range(n-1):
            for j in range(i+1, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    did_swap = True
                else: break
            if not did_swap: break
        return arr

    @staticmethod
    def recursion_sort(arr, n=0):
        did_swap = False
        if n == len(arr)-1:
            return arr
        for i in range(n+1, 0, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                did_swap = True
            else: break
            if did_swap is False: return arr
        return InsertionSort.recursion_sort(arr, n+1)


iso = InsertionSort()
print(iso.sort([4, 2, 7, 95, 25, 47, 1, 3]))
print(iso.sort([1, 2, 3, 4, 5, 6, 7]))

print(iso.recursion_sort([4, 2, 7, 95, 25, 47, 1, 3]))
print(iso.recursion_sort([1, 2, 3, 4, 5, 6, 7]))

# time complexity: O(n^2) - worst and average case scenarios
#                : O(n) - best case scenario when array is already sorted
# space complexity: O(1)


