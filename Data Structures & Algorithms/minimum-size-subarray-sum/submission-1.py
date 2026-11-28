'''
-  integer arrays nums
- positive integer target
- return the minimal lenght of a contigous subarray where values >= target

--

approach:

[2,3,7,2,1,9,12] = target 12

brute force: iterate from i and create a window with j values: if windowSum >= target: windowLength = min(windowLength, curWindowLength)

--

create left and right pointers, if window >= target l+=1 else window <target r+=1, if windowLength = min(windowLength, curWindowLength)


'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        windowLen = float('inf')
        curr = 0

        for r in range(len(nums)):
            curr+= nums[r]

            while curr>= target:
                windowLen = min(windowLen, r-l+1)
                curr-=nums[l]
                l+=1



        return 0 if windowLen == float('inf') else windowLen
            
        