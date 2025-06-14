class Solution:
    def mostFrequentElement(self, nums):
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        max_frequency = max(frequency.values())
        maximum_matches = [key for key, value in frequency.items() if value == max_frequency]
        return min(maximum_matches)

sol = Solution()
print(sol.mostFrequentElement([1, 2, 2, 3, 3, 3]))