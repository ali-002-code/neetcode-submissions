class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                min_height = min(heights[i], heights[j])
                area = min_height * (j-i)
                areas.append(area)
        return max(areas)

        