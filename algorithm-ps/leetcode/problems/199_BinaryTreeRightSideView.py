""" https://leetcode.com/problems/binary-tree-right-side-view/description/
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []
"""

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = deque([root])
        
        while q:
            level_size = len(q)
            current_nodes = []
            
            for _ in range(level_size):
                node = q.popleft()
                current_nodes.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(current_nodes[-1].val)

        return result

