'''

Input: coins = [1,2,3,6,8], amount = 14

we need to identify how many coins it take at a minimum to make a coin at a certian value

to make 1 we need 1 coin
to make 2 we need amount_for_one_coin +1 -> dp[1]+1 -> dp[2] = 2 or the minimum value of itself which is 1

we continue this pattern till we reach dp[amount]

Output: 3

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount +1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >=0:
                    dp[a] = min(dp[a], 1+ dp[a-c])


        return dp[amount] if dp[amount] != float('inf') else -1
        