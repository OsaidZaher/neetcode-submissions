# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''

- each house has only one parent (each node has exactly one parent)
- if two directly linked houses were broken the police will be contact
- return max that can be broken into before the police comes

examples:

beginning at the root iterate through left subtree if exists
if not go right then repeat

1-> 2 -> 3 -> 4 

save left and right val and return max to parent
max(4,2) -> 4 return 4 to parent



'''



class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root):

            if not root:
                return [0,0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            withRoot = root.val + left[1] + right[1]
            withoutRoot = max(left) + max(right)

            return [withRoot, withoutRoot]
        
        return max(dfs(root))


        