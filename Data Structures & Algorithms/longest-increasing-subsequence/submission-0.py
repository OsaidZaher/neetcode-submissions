'''
- so we are given an integer array nums
- a subsequence is a sequence where elements are a position ahead of each other, but not strictly by 1
- return longest subsequence where the numbers are increasing in order
- not sorted
- strictly increasing
- we have duplicates
- array may be empty

Input: nums = [1,4,2,3,3,7,9]

Output: 4


--

currentMax = 4
iterating through every index i we see if next is greater, if true increase count
next = prev we do this for every value in j 0(2^n)

--
dp[0] = [0]
dp[1] = dp[1]
dp[i] = max(dp[i-1], dp[i-2]+1)




'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        lis = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j]+1)

        return max(lis)
        