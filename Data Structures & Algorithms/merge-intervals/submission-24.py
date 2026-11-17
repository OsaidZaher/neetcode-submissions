'''
you are given an array of intervals, where each element of the array is
intervals[i] = [start_i, end_i]

your task is to merge the overlapping intervals t

where an overlapping integer is when 2 points have one same value

--

approach:

Input: intervals = [[1,3],[1,8],[6,8] [7,9]]

we sort the array and we created a merged array that is empty

we then check if merged is empty: if true we can just add the intervals cus no comparison to be made
if merged is not empty:  -> merged = [[1,3]] 
check if end >= start: if true merge [1,3] which is the top of the stack

return we merged





'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        interval = sorted(intervals, key=lambda x:x[0])

        merged = []

        for start, end in interval:
            if not merged or start > merged[-1][-1]:
                merged.append([start,end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged



        
                
                    
        



