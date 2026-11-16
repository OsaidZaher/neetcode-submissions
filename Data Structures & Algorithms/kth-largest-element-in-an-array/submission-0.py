'''

given an array called nums 
given an integer called k  
return the kth largest element in the array 

- 
approach


[2,3,1,5,4], k = 2

if you sort this and return the kth -1 index you are finished

--

beginning at index 0 give it rank 1
check between 2 and 3 since 3>2 3 is 1st and 2 is 2nd
compare 1 to 3 and then 2...

o(n)^2

--



'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = sorted(nums, reverse=True)
        return nums[k-1]
        