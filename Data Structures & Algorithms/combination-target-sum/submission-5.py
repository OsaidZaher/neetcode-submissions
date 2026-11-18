class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        cur = []
        res = []
        total = 0

        def dfs(i, cur, total):

            if i >= len(nums) or total > target:
                return 
            if total == target:
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, cur, total)
        return res