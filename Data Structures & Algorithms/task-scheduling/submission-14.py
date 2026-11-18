'''
- array of capitalCase characters for each position in tasks
- integer n 
- cpu cycle = 1 task -> any order
- constraint is that tasks with same letter must be seperate by n cycles
- return minimum cpu cycles

-- 

approach:

Input: tasks = ["X","X","Y","Y","Y"], n = 2

create a hashMap with counts of x and y

countVals = {x:[2,0], y: [3,0]}

take 





'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0

        q = collections.deque()

        while maxHeap or q:
            time +=1
            
            if maxHeap:
                cnt = 1+ heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time





        