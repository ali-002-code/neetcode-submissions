#have left and right pointers
#pass right thru list and add each element to set
#length of substrung is distance between left and right sunbstrings
#when item found that is already in set, shrink list and remove item from set until no duplicates
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        res = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res

        