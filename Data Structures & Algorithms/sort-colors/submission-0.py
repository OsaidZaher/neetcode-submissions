'''

You are given an array nums consisting of n elements where each element is an integer representing a color:
0 represents red
1 represents white
2 represents blue

-
Input: nums = [1,0,1,2]
Output: [0,1,1,2]

hashmap = {0:1, 1:2, 2:1}

so we know the array is of size n 
values in the hashmap 0,1,2

what if we iterate through keys 0->1->3 using 3 for loops
each loop adds to some array / replaces value in nums 
copy array into other or finish replacement

--
hashmap = {0:1, 1:2, 2:1}

counter = 0

while hashMap[0]:
    hashMap[0]-=1
    res[counter] == 0
    counter+=1


while hashMap[1]:
    hashMap[0]-=1
    res[counter] == 0
    counter+=1

while hashMap[2]:
    hashMap[0]-=1
    res[counter] == 0
    counter+=1


'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashMap = defaultdict(int)
        counter = 0

        for num in nums:
            hashMap[num]+=1

        while hashMap[0]:
            hashMap[0]-=1
            nums[counter] = 0
            counter+=1
        
        while hashMap[1]:
            hashMap[1]-=1
            nums[counter] = 1
            counter+=1
        
        while hashMap[2]:
            hashMap[2]-=1
            nums[counter] = 2
            counter+=1
        

        
        