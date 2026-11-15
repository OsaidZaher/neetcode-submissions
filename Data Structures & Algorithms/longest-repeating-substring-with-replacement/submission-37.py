class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashMap = defaultdict(int)
        l = 0
        maxRes = 0

        for r in range(len(s)):

            currentWindow = abs(l-r) +1
            hashMap[s[r]]+=1

            while abs( currentWindow - max(hashMap.values())) > k:

                hashMap[s[l]]-=1
                l+=1
                currentWindow = abs(l-r) +1
            
            maxRes = max(currentWindow, maxRes)
        
        return maxRes



        
        