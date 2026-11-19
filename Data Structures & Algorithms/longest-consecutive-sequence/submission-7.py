class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
  
        nonDupNums = sorted(set(nums))
        if not nonDupNums:
            return 0

        currLength = 1
        maxLength = 1

        for i in range(1, len(nonDupNums)):
            if nonDupNums[i] - nonDupNums[i - 1] == 1:
                currLength += 1
            else:
                currLength = 1
            maxLength = max(maxLength, currLength)

        return maxLength
        