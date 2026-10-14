'''
- sorted non desc order
- return vals in index1 and index2 that add to target where index1 < index2
- there will always be a valid solution


--
approach

Input: numbers = [1,2,2,3,4,6,7], target = 5

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) -1

        while l < r:

            if numbers[l] + numbers[r] == target :
                valA = l+1
                valB = r+1
                return [valA, valB]
            elif numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            
        