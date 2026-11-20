
'''

- given array prereq -> prereq[i] = [a,b] where b needs to be taken first before a
- we have numCourses amount to take courses are labelled from 0 - numCourses-1
return true if you can finish all courses
-

-- approach

prerequisites = [[0,1],[1,2],[0,2]] 

hashMap: {0:[1,2], 1:[2],2:[]}

- if a key is found inside of a prereq array of one its prereq we can return false

- beginning at nums -> go to key -> add key to visiting then go to neighbours
check neighbours of 1 mark 1 as visiting 
if neighbour of 1 is in visiting return false
if the neighbour has none mark as complete 


- create a dfs function that takes in node 
- if node in visiting, return false
- if node is completed return true 
- hashMap[node] = node
mark node as visiting 
for n in node.neighbours
if not dfs(n): return false




'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = defaultdict(list)
        visiting = set()
        

        for course, pre in prerequisites:
            hashMap[course].append(pre)

        def dfs(course):
            if course in visiting:
                return False
            if hashMap[course] == []:
                return True
            visiting.add(course)
            for pre in hashMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            hashMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        