# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Idea: level order traversal 
# 1. what I need: a cur level queue, next level queue 
# 2. 
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        while q:
            cur_len = len(q)
            right_node = q.popleft()
            res.append(right_node.val)
            if right_node.right:
                q.append(right_node.right)
            if right_node.left:
                q.append(right_node.left)  
            for i in range(cur_len - 1):
                right_node = q.popleft()
                if right_node.right:
                    q.append(right_node.right)
                if right_node.left:
                    q.append(right_node.left) 
        return res                       
                
