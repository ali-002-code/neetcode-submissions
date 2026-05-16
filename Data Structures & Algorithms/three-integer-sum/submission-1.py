class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort nums so order
        result = []
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #use left and right pointer for each number and make left and right sum to number
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
        