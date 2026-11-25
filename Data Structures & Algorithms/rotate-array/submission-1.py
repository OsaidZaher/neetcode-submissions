'''
- you are given an integer array nums, 
- your task is to rotate the array k steps where k is a positive integer
- we can assume a fixed size array with any integer value
- our task it to move the end value at each rotation to front
- k can be larger than array size


--
approach

iterating k time:
res = []
value = nums[-1]
res = nums[:-1] 
res = deque()
res.append(value)





'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        def rotate(l,r):

            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1

        rotate(0, len(nums)-1)
        rotate(0, k-1)
        rotate(k, len(nums)-1)


        