class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def max_contain(node):
            nonlocal max_sum
            if not node:
                return 0
            max_left = max(0, max_contain(node.left))
            max_right = max(0, max_contain(node.right))
            max_sum = max(max_sum, max_left + node.val + max_right)
            return node.val + max(max_right, max_left)
        max_contain(root)
        return max_sum
        