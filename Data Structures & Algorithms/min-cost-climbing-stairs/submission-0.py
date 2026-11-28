'''

- you are given an array of integers cost where cost[i] is the cost of each step
- your task is to reach the top of the stairs taking 1 or 2 steps while concurring the least amount of cost, cost[i+1], cost[i+2]
- you may begin on the first stair cost[0] or second stair cost[1]
- 

--
Input: cost = [1,2,1,2,1,1,1]

[1][2][2][4][3][4][5]

- initilise a results array with just empty arrays res = [0] * len(cost)
- res[0] = cost[0], res[1] = cost[1]
- we iterate over 2nd value to end of cost
- we compute the position in res of i value (2nd) to be minimum of itself+res[i-1] and itself+[i-2]
- return final value 

for i in range len(2,nums):
    res[i] = min()
    ]]
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2,len(cost)):
            dp[i] = min((cost[i]+dp[i-1]), (cost[i]+dp[i-2]))

        return min(dp[-1], dp[-2])
        