# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function that checks if node is within (low, high) boundaries
        def validate(node, low, high):
            # Base case: an empty node is valid
            if not node:
                return True
            
            # The current node's value must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # Recursively check left and right subtrees with updated boundaries
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        # Start with negative and positive infinity as initial bounds
        return validate(root, float('-inf'), float('inf'))