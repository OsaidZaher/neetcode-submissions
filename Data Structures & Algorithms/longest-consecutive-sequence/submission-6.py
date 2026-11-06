class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numbers = set(nums)
        res = []

        for num in numbers:
            if num - 1 not in numbers:
                row = []

                while num in numbers:
                    row.append(num)
                    num += 1

                res.append(row)

        return max((len(row) for row in res), default=0)
        
            