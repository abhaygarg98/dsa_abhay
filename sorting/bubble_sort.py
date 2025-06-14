class BubbleSort:

    def sort(self, arr):
        n = len(arr)
        did_swap = False
        for i in range(n-1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    did_swap = True
            if not did_swap: break
        return arr

    @staticmethod
    def recursive_sort(arr, n=None):
        did_swap = False
        if n is None:
            n = len(arr)
        if n == 1:
            return arr
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                did_swap = True
        if not did_swap: return arr
        return BubbleSort.recursive_sort(arr, n-1)


bs = BubbleSort()
print(bs.sort([126, 95, 15, 84, 9, 7]))
print(bs.sort([0, 1, 2, 3, 4, 5]))

print(bs.recursive_sort([126, 95, 15, 84, 9, 7]))
print(bs.recursive_sort([0, 1, 2, 3, 4, 5]))

# time complexity: O(n^2) - worst and average case scenarios
#                : O(n) - best case scenario when array is already sorted
# space complexity: O(1)