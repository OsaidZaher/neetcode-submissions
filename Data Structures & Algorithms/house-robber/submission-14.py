
'''

- given an array of ints: nums, 
- where nums[n-1] and nums[n+1] are neighbours of nums[n]
- return maxTotal if you cant rob neighbours

-- 
example + approach:

Input: nums = [1,1,3,3]

- you can choose to rob i or not 
- if you rob i -> cant rob i+1 

choice include 1 or not 
include:[1], not_include_1:[]
choice include [1]
[1], [1]
choice include 3 or not
include_1: [1,3] not_include_1 : [1]

choice include 3 or not
include_1: [1,3] not_include_1 : [1,3]

[2,9,8,3,6]

max of 2,9 = 9
max of 2+8, 9 = 10
max of 10, 9+3 = 12
max of 10+6, 12 = 16

have an empty array of just 0s of length nums 

we are replacing the index of this array that has 0 with max of position it is in and and prev + next

return the -1 index

[2,9,8,3,6,7]

[0][0][0][0][0]

[[2, 0+9]], [9, 2+8], [10, 9+3], [12, 10+6], [16, 12+7]


'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i])

        return dp[-1]



        
            
            
        