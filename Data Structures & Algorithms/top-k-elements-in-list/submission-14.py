'''
Rephrase:

- we are given an array of integers called nums
- we are given an integer called k
- we are to return the k amount of elements that are most frequent in the array
- we can assume that we will not have not the same integer in the same output more than once

Approach:

Beginning at index 0 iterate thorugh the array
we get the value the value and append its current count if it previously appeared, if not we initiate its count to 1
we can sort the numbers by their count and return the k elements at the top

create a hashMap with a default value of 0 
iterating through nums we appends num counter in hashMap
return the k most frequent keys

return res[1][:k]

'''



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = defaultdict(int)

        res = []
        seen = set()

        # hashMap = { 1:1, 2:2, 3:3 }

        for num in nums:
            hashMap[num] = 1 + hashMap[num]

        for num in nums:
            if num not in seen:
                res.append([num, hashMap[num]])
                seen.add(num)


        res.sort(key = lambda x: x[1], reverse=True)

        return [item[0] for item in res[:k]]

        

        
            


        
        