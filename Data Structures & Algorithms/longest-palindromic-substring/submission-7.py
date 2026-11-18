class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        longestS = ''

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > maxLength:
                    maxLength = (r - l) + 1
                    longestS = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > maxLength:
                    maxLength = (r - l) + 1
                    longestS = s[l:r+1]
                l -= 1
                r += 1

        return longestS