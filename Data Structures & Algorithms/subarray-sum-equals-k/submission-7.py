class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        summ = 0
        prefix = {0:1}

        for n in nums:
            summ += n
            diff = summ - k

            res+= prefix.get(diff, 0)
            prefix[summ] = 1 + prefix.get(summ, 0)

        return res
        