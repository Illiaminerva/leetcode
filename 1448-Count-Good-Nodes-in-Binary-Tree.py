# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def helper(root, max_val):
            nonlocal total
            if not root:
                return None
            if root.val >= max_val:
                total += 1
                max_val = root.val
            helper(root.left, max_val)
            helper(root.right, max_val)
        helper(root, float("-inf"))
        return total
