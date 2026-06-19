class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            area = heights[i]
            for j in range(i-1, -1, -1):
                if heights[j]>= heights[i]:
                            area = area + heights[i]
                else: break
            for k in range(i+1, len(heights)):
                if heights[k]>= heights[i]:
                            area = area + heights[i]
                else: break
            if area > max_area:
                max_area = area
        return max_area
