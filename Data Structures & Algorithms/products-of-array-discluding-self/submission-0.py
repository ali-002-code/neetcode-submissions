class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            result = 1
            for j in range(0, i):
                result = result * nums[j]
            for z in range(i+1, len(nums)):
                result = result * nums[z]
            output.append(result)
        return output
        