'''
- given array called nums 
-  given an integer called k
-  retrun the  k most frequent elements
- you can expect the answers to always be unique 
- you are to return the integers in any order

--

Input: nums = [2,2,3,2,4,4,4,4], k = 2

hashMap = {2:3, 3:1, 4:4} 

time: 0(n) + 0(nlongn) -> 0(2n)-> 0(n), space: 0(2n) -> o(n)

return the keys with the top k values

- create a hashMap 
- iterate through nums increment num_key count 
- iterate through hashmap add key and value to a result array

res = [,,] 
res = [[4,4],[2,3], [3,1]]

sort based on x[1] and return items[0] up to k-1


'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        numCount = defaultdict(int)
        res = []

        for num in nums:
            numCount[num] += 1

        for key, val in numCount.items():
            res.append([key, val])

        res.sort(key=lambda x: x[1], reverse=True)

        return [item[0] for item in res[:k]]

        

        