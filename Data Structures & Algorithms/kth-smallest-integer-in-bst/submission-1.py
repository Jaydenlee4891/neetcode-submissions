class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # We will use this variable to store our answer when we find it
        ans = None
        
        def inorder(node):
            nonlocal k, ans
            # Base case: if node is None or we already found the answer, stop
            if not node or ans is not None:
                return
            
            # 1. Go as far Left as possible (smallest values first)
            inorder(node.left)
            
            # 2. Process the current Root (decrement our k countdown)
            k -= 1
            if k == 0:
                ans = node.val
                return
            
            # 3. Go Right if k hasn't hit 0 yet
            inorder(node.right)
            
        inorder(root)
        return ans