class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        i = 0
        maxRes = 0

        for j, char in enumerate((s)):
            while char in seen:
                seen.remove(s[i])
                i+=1
            
            seen.add(char)
            maxRes = max(maxRes, (abs(j-i)+1))

        return maxRes
        