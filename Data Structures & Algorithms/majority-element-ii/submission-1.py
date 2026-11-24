'''
- you are given an integer array of size n 
- find all elements that appear more than n/3 time 
- return result in any order
- n is the size of n -> n appears more than any element count
- positive negative integers
- we can assume 1 value in the array
- a million
- counter counts every instance of unique values 


10/3 = 3
count = {5:4, 2:5,3:1}

--

approach:

approach A:

Input: nums = [1,1,1,2,3,4,5,6,6,6,1] -> 

Output: [1]

check = n/3 11/3= 3.666
iterate through nums if i == next increment count 
we can convert count into floats compare each count to check: add if greater

0(n^2)
--
Input: nums = [1,1,1,2,3,4,5,6,6,6,1] -> 

Output: [1]

count = 
{1:4, 2:1,3:1,6:3,} 

- create a hashMap with count of num vlaues
- setify nums/ create visited set
- iterate through nums if num.value > check : res.append(nums)


time: 0(n) space: o(n)


- iterate through nums if num.value > check and num not in visisted: res.append(nums)
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        check = len(nums)/3
        count = Counter(nums)
        nums = set(nums)
        nums = list(nums)

        
        res = []

        for num in nums:
            if count[num] > check:
                res.append(num)

        return res
        