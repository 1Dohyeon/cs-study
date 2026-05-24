""" https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=problem-list-v2&envId=tree
103. Binary Tree Zigzag Level Order Traversal
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        result = []
        level = 0

        # 짝수 층: 왼쪽에서 오른쪽
        # 홀수 층: 오른쪽에서 왼쪽

        while q:
            level_size = len(q)
            current_nodes = []
            
            # 현재 층에 있는 노드들만 다 꺼내서 처리
            for _ in range(level_size):
                node = q.popleft()
                current_nodes.append(node.val)
                
                # 다음 층 노드들을 미리 큐에 넣어둠 (항상 왼쪽부터)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # 홀수 레벨이면 리스트를 뒤집음
            if level % 2 == 1:
                current_nodes.reverse()

            result.append(current_nodes)
            level += 1 # 다음 층으로 이동
        
        return result