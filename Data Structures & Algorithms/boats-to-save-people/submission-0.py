'''

- int people -> people[i] = weight
- you have an infinite amount of boats, but each boat has a weight limit
- each boat has a capacity of 2, and sum of weights <= capacity
- return the minimum number of boats to carry every person
-you can assume capcity > max(people)
- assume it is populated by at least one person
- its not sorted

-- 

Input: people = [2,1,4,5], limit = 7

Output: 2

brute force:
beginning at index 0 i will gaurantee they are leaving ill compare to every other value and if  capcity - index 0 <= capcity i will save this as current we will set current to max(itself, otherValue)
0(n)^2

--









'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1

        return boats
        