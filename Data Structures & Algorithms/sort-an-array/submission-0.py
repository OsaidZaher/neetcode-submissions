'''

you are given an integr array nums sort it in ascending order
solve without any inbuilt functions 
- any integers
- always populated
- it seems we can have duplicates
- array not sorted

--

approach

[10,9,1,1,1,2,3,1] 

10:1, 9:1, 1:4, 3:1, 

 



'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        hashMap = defaultdict(int)
        minVal = min(nums)
        maxVal = max(nums)
        res =[]

        for num in nums:
            hashMap[num]+=1

        for val in range(minVal, maxVal +1):
            while hashMap[val]:
                res.append(val)
                hashMap[val]-=1
        return res


        