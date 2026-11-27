# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- you are given a bst tree -> left < parent < right
- return root node/ return tree after insertion of the node

-- 
[5,3,9,1,4], val = 6

left < parent < right
-inf < parent < inf

left: -inf < node < leftNode :3
right: leftNode:3 < node < 5

create bounds for each node
the bound is initially -inf and inf
the node has to satisfy being inside these bound, they update based off of the tree
left: left, root.val, right
right: left, right root.val

we begin the base case if there are no nodes and we make this check to add



'''


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        if val> root.val:
            root.right = self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        
        return root

        