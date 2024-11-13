"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict 
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = [node]
        old_to_new = {node: Node(node.val)}
        
        while queue:
            cur_node = queue.pop(0)
            
            for neighbor in cur_node.neighbors:
                if neighbor not in old_to_new:  # Create new node only if it hasn't been created before
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Connect the current node to its neighbor
                old_to_new[cur_node].neighbors.append(old_to_new[neighbor])
                
        return old_to_new[node]

            
            
        
        
        
