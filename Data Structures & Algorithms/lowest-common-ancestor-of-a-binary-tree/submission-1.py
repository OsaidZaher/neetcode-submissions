# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
you are given a binary tree
your task is to return the lowest common ancestor of two nodes in said tree

given 2 values p and q, the lca is the node most deep in the tree that has p and q as descendants

p or q can also be the lca

-- 

approach

check the current node and see if it is equal to p or q 
if not check its left and right.

continue doing this until both p and q are found, the lca is the parent of the one with the shallower depth

p = 4 q = 2

if tree is none return none

is 5 p or q? no go to left
is 3 p or q no go to left
is 2 p or q yes -> return p 
no more left we reach end
go to paren and check right side
1 not p or q we reach end back to parent or 3
back to 5 then we go to right
is 4 p or q yes -> return 4

4 is at a higher level than 2 so the lca has to be parent of 4 which is 5

lca = 5



'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        if root is None:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if root is p or root is q:
            return root
        
        if left and right:
            return root
        
        if left and not right:
            return left

        return right
        