class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1
        window = defaultdict(int)
        left = 0
        have = 0
        need = len(t_count)
        # store best window
        res = [-1, -1]
        res_len = float("inf") #set to infinity
        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            if char in t_count and window[char] == t_count[char]:
                have +=1  
            while have == need: #shrink list
                if (right - left + 1) < res_len: #check if window shortest
                        res = [left, right]
                        res_len = right - left + 1
                window[s[left]] -= 1 #remove left charagter from window
                if s[left] in t_count and window[s[left]] < t_count[s[left]]: #if char in both lists check enough
                    have -= 1 #dont have enough
                left += 1
        left, right = res
        return s[left:right+1] if res_len != float("inf") else ""
        
        
        

        