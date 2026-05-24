class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        for left in range(len(nums)- k + 1):
            right = left + k - 1
            window = []
            for i in range(left, right + 1):
                window.append(nums[i])
            res.append(max(window))
        return res
            
