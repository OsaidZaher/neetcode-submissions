class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        currSum, res = 0,  0
        hashMap = defaultdict(int)
        hashMap[0]+=1

        for num in nums:
            currSum +=num
            diff = currSum - k
            res+= hashMap[diff]
            hashMap[currSum]+=1
        
        return res
        