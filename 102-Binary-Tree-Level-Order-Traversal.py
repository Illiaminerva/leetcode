# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict 
# Recursion approach
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        result = []
        q = collections.deque()
        q.append(root)
        while q:
            cur_level = []
            for i in range(len(q)):
                node = q.popleft()
                cur_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(cur_level)
        return result






        
        
        


