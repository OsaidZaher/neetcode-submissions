class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        res = defaultdict(int)

        for num in nums:
            res[num]+=1


        res = sorted(res.items(), key= lambda x:x[1], reverse=True)

        return res[0][0]

       
        