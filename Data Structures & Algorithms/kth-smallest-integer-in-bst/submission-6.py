# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def DFS(root, arr):
            if not root:
                return None
            if root.left:
                DFS(root.left,arr)
            arr.append(root.val)
            if root.right:
                DFS(root.right,arr)
            return arr

        arr = []
        DFS(root,arr)
        return arr[k-1]