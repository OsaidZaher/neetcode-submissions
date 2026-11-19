
'''
rephrase:

- given an array nums, return amount of subarrays where total == k
- subarray =  elements in array back to back
- can include negatives
- at leat 1 solution
- not sorted array

--
approach + examples

[2,-1,1,2], k = 2

- iterate over i, iterate over j, if total == nums res +=1 o(n)^2

[-1,1,2,2] k = 1

while less than k increment r

--

lets say we make a hashMap 

each key has the sequence value it needs to get k

2:0, -1:3, 1:1, 2:0,0:0



'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hashMap = defaultdict(int)
        hashMap[0]+=1
        res = 0
        curSum = 0

        for num in nums:
            curSum +=num
            diff = curSum -k

            res += hashMap[diff]
            hashMap[curSum]+=1
        
        return res



        