class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[pre].append(crs)            

        preMap = {}

        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()
                for nxt in adj[crs]:
                    preMap[crs] |= dfs(nxt)
                preMap[crs].add(crs)
            return preMap[crs]

        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(v in preMap[u])      
        return res
                