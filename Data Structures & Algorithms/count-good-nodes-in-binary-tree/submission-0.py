# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def DFS(root,biggest_val):
            if not root:
                return 0
            res = 1 if root.val >= biggest_val else 0
            biggest_val = max(biggest_val, root.val)
            res += DFS(root.left, biggest_val)
            res += DFS(root.right, biggest_val)
            return res

        return DFS(root, root.val)

