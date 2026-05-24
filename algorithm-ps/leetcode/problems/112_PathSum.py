""" https://leetcode.com/problems/path-sum/description/?envType=problem-list-v2&envId=tree
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS 재귀 풀이
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # 리프 노드를 찾을 수 없으면, 현재 노드의 value와 targetSum이 같다면 true 반환 - 자식 노드로 갈때마다 targetSum에서 현재 노드의 value를 뺄 예정
        if not root.left and not root.right:
            return root.val == targetSum
        
        # 왼쪽, 오른쪽 자식 노드로 재귀 호출 - targetSum에서 현재 노드의 value를 뺀 값을 넘겨줌
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    
# BFS 풀이
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
        
#         queue = deque([(root, targetSum - root.val)])
        
#         while queue:
#             node, curr_sum = queue.popleft()
#             # 리프 노드에 도달했을 때, 현재까지의 합이 targetSum과 같다면 true 반환
#             if not node.left and not node.right and curr_sum == 0:
#                 return True
            
#             if node.left:
#                 queue.append((node.left, curr_sum - node.left.val))
#             if node.right:
#                 queue.append((node.right, curr_sum - node.right.val))
        
#         return False