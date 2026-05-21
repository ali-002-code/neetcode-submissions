#use window sliding method to look at each window
#for each window, get most frequent value
#see if enough k values to make a longer list (compare windth of window - most frequent) - keep changing left pointer use a while loop
# enough k values add length of window to res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        count = {}
        for right in range((len(s))):
            count[s[right]] = 1 + count.get(s[right], 0)
            while ((right - left + 1) - max(count.values()))> k:
                count[s[left]] -= 1
                left +=1
            res = max(res, right-left+1)
        return res
        