""" https://leetcode.com/problems/populating-next-right-pointers-in-each-node/?envType=problem-list-v2&envId=breadth-first-search
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from tables import Node
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque([root])

        while q:
            level_size = len(q)

            for i in range(level_size):
                # 큐에서 현재 노드를 꺼냄
                node = q.popleft()
                
                # 현재 레벨의 마지막 노드가 아니라면, 
                # 큐의 맨 앞에 있는 노드가 같은 레벨의 바로 오른쪽 노드임
                if i < level_size - 1:
                    node.next = q[0]
                
                # 자식 노드가 있다면 큐에 추가 (완전 이진 트리이므로 왼쪽이 있으면 오른쪽도 있음)
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
                    
        return root