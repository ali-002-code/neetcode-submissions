class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortd = sorted(nums)
        longest = 1
        count = 1
        for i in range(len(sortd) - 1):
            # skip duplicates
            if sortd[i] == sortd[i + 1]:
                continue
            if sortd[i + 1] == sortd[i] + 1:
                count += 1
            else:
                longest = max(longest, count)
                count = 1
        longest = max(longest, count)#new longest made to count of count larger than current longest
        return longest