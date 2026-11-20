class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        visited = set()

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):     
            visited.add(node)
            for val in graph[node]:
                if val not in visited:
                    dfs(val)

        count= 0


        for node in range(n):
            if node not in visited:
                dfs(node)
                count+=1
        
        return count



        