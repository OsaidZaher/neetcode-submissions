class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        maxRes = 0
        i = 0

        for j, char in enumerate(s):
            while char in seen:
                seen.remove(s[i])
                i+=1
            seen.add(char)
            maxRes = max(maxRes, (abs(i-j)+1) )
        return maxRes