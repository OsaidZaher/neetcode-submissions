# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
you are given a root of a tree your task is to ensure that it is a valid bst

a bst has the properties

all left subtrees are less than root
all right subtrees are greater than root

return true or false


approach:

beginning at root traverse left subtrees till reach bottom/ base case
if left subtree < root continue returning left to parent
parent then go down to right subtree if right > parent continue

continue doing this till you reach the parent node, if either check are false break 



'''


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left, right):

            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float('-inf'), float('inf'))

            