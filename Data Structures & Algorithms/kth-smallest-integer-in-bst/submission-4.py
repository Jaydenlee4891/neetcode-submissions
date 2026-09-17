class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root, arr):
            if not root:
                return
            
            if root.left:
                traverse(root.left, arr)
            arr.append(root.val)
            if root.right:
                traverse(root.right, arr)
        
        arr = []
        traverse(root, arr)

        return arr[k-1]