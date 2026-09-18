# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # 1. Map every value in inorder to its index for O(1) lookups
    inorder_map = {val: i for i, val in enumerate(inorder)}

    # Keep track of where we are in the preorder list
    pre_idx = 0

    def helper(left: int, right: int) -> Optional[TreeNode]:
      nonlocal pre_idx

      # Base case: if there are no elements to construct a subtree
      if left > right:
        return None

      # Grab the current root value from preorder, then advance the pointer
      root_val = preorder[pre_idx]
      pre_idx += 1
      root = TreeNode(root_val)

      # Find where this root splits the inorder list in O(1) time
      mid = inorder_map[root_val]

      # Recursively build left and right subtrees using boundary pointers
      root.left = helper(left, mid - 1)
      root.right = helper(mid + 1, right)

      return root

    return helper(0, len(inorder) - 1)
            