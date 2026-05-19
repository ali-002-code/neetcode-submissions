#start with pointers on out side
#shrink lower value down and see if you can find a larger value as that will be where water is trapped
#when u find the other max value, subtract height of pill for water ontop
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 #left pointer position
        right = len(height) - 1 #right pointer position
        left_max = height[left] #left pointer value
        right_max = height[right] #right pointer value
        res = 0
        while left < right:  
            if left_max < right_max:  #if right value larger
                left += 1 #shift left pointer along
                left_max = max(left_max, height[left]) #see if new value of left pointer greater than current value
                res += left_max - height[left] #water above will be maximum left value - height of pill
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res