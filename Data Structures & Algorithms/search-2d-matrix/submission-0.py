class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            # Only search the row if target could be inside it
            if row[0] <= target <= row[-1]:
                left = 0
                right = len(row) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
        return False
