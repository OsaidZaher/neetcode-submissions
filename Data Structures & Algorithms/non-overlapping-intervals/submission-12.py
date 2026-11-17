
'''

you are given an itervals where intervals[i] = [start_i, end_i]
return the minimum amount of intervals to be removed such that no interval is overlapping

--
create a seperate array where we are holding the remaining values 
if we merge values together and add it to a res array then we have how many values are left after merging if we see the difference in both arrays then we can get minRemovals

input = [[1,2],[1,4], [2,4], [2,5], [1,6]]

sort inputs = [[1,2], [1,4],[1,6], [2,4], [2,5] ]

merge 1,2 and 1,4 -> 1,4 then merge 1,4 with 1,6 get 1,6
mege 2,4 with 2,5 get 2,5

merged array = [[1,6], [2,5]]

abs(len(merged) - len(inputs)) = 


'''




class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])

        removals = 0
        prev_end = float("-inf")

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removals += 1

        return removals

        

        