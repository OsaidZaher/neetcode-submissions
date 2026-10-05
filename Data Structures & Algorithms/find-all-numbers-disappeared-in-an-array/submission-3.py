class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

       
        sets = set()

        for num in nums:
            sets.add(num)

        
        output= []
        i = 0

        while i < len(nums):
            
            if i+1 not in sets:
                output.append(i+1)

            i+=1
        
        return output
        