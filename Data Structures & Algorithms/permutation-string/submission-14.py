class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count1, count2 = defaultdict(int),defaultdict(int)

        for char in s1:
            count1[char]+=1
        
        left = 0

        for right, char in enumerate(s2):

            count2[char]+=1

            if abs(left - right) + 1 > len(s1):

                count2[s2[left]]-=1
                if not count2[s2[left]]:
                    del count2[s2[left]]

                left+=1
            
            if count1== count2:
                return True

        return False






