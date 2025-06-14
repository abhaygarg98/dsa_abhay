class MergeSort:

    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = MergeSort.sort(arr[:mid])
        right_half = MergeSort.sort(arr[mid:])

        return MergeSort.merge(left_half, right_half)  # Merge sorted halves

    @staticmethod
    def merge(left, right):
        sorted_arr = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        sorted_arr.extend(left[i:])  # Append remaining elements
        sorted_arr.extend(right[j:])  # Append remaining elements

        return sorted_arr

ms = MergeSort()
print(ms.sort([6, 4, 1, 3, 8, 9]))


# time complexity: O(nlog(n))
# space complexity: O(n)

