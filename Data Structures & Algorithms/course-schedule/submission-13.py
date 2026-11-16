class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        prereq = prerequisites
        state = [0]* numCourses

        for a, b in prereq:
            adj[a].append(b)

        def dfs(course):

            if state[course] == 1:
                return False
            elif state[course] ==2:
                return True

            state[course] = 1

            for n in adj[course]:
                if not dfs(n): return False
            
            state[course] =2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


        