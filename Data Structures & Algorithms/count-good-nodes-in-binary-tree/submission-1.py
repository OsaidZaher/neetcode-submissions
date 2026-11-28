# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
- good node x = path from root to x contains no nodes greater than x 
- given the root of tree return the count of good nodes in the tree

--
approach:

- call dfs on children,
- base case is when node is none return
- we return node.value to parent 
- 


'''



class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if maxVal <= node.val else 0
            maxVal = max(node.val, maxVal)
            res+= dfs(node.left, maxVal)
            res+= dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)

        