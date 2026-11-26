'''
- 2 integers n and k 
- return all possible combinations of k numbers
- the range of numbers begins from 1 to n

-- 
approach:

Input: n = 4, k = 1

Output: [
    [1,2],
    [1,3],
    [2,3]
]

'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def dfs(start, comb):
            if len(comb) == k:
                res.append(comb[:])

            for i in range(start, n+1):
                comb.append(i)
                dfs(i+1, comb)
                comb.pop()

        dfs(1, [])
        return res
        