class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        from collections import defaultdict
        s1_dict = defaultdict(int)
        window = defaultdict(int)
        for char in s1:
            s1_dict[char] += 1
        left = 0
        for right in range(len(s2)):
            window[s2[right]] += 1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if window == s1_dict:
                return True
        return False



            

