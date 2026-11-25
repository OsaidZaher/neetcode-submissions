'''
- we are given an array of weights, each element displays a weight value
- we are given a constraint of days were all elements have to be shipped
- we are to return the minimum capacity required to remove all elements within integer days
- days has to be at least a positive integer
- weights are all positive integers

Input: weights = [1,2,3,4,5,6,7,1], days = 5

Output: 

- we know maximum capacity >= max(weights) 
- i checked the length of the array which was equal to length of days hence i just returned maximum value



'''


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l, r = max(weights), sum(weights)
        res = r

        def canShip(capacity):
            ships, currCap = 1, capacity
            for w in weights:
                if currCap  - w < 0:
                    ships +=1
                    currCap = capacity
                currCap -= w
            return ships  <= days


        while l<=r:
            capacity = (l+r)//2
            if canShip(capacity):
                res = min(res, capacity)
                r = capacity-1
            else:
                l = capacity+1

        return res
        