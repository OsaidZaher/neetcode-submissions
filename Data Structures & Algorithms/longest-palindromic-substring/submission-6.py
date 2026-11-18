'''
- a palindrome is a string that is the same both backwards and forwards
- given a string s return the longest length of the palindrome

--

approach:

beginning at index 0 for i and index +1 for j check if a+b is a pal if true increase max res to prev and itself

how to check if pal
if string backwards = string forward is palindrome 



'''


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s[0]

        longestString = ''

        for i in range(len(s)-1):
            j = i+1
            for j in range(len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(longestString):
                    longestString = s[i:j+1]

        return longestString
        