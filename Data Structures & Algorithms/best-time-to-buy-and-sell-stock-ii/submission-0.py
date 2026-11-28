'''
- you are given an array prices where price[i] is value in current day
- you may buy and sell stocks on the same day but can hold only one stock concurrently
- you have an infinite number of operaitons.
-return the maximum amount of money you can make
- assume positive ints and 0
- we will have a single value at least
- array not necessarily sorted

--
approach

[7,1,5,3,6,4]





'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += abs(prices[i-1]- prices[i])


        return profit
        