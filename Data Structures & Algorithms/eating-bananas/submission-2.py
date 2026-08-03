class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right
        while left <= right:
            k = (left + right) // 2
            eating_time = 0
            for pile in piles:
                eating_time += math.ceil(pile / k)
            if eating_time <= h:
                answer = k
                right = k - 1
            else:
                left = k + 1
        return answer