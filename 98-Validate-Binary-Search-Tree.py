class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, min_value, max_value):
            if not root:
                return True
            if not min_value < root.val < max_value:
                return False
            return validate(root.left, min_value, root.val) and validate(root.right, root.val, max_value)
        return validate(root, float("-inf"), float("+inf"))