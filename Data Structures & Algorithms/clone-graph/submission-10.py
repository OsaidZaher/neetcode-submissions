"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
- create a hashmap to store the copies
- check if a deep copy of node is in the hashmap if not we have to make one, if is there we can just return it

make new copy:
copy is the creation of a new node object with val
add this to hashmap wit key node 
now you have the neighbours of said node, iterate through them
call the dfs function adding the copies as neighbours 
return copy with all neighbours

call dfs

'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}
        def dfs(node):

            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh)) 
            return copy
        
        return dfs(node) if node else None
        