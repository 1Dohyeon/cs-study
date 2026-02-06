""" https://leetcode.com/problems/validate-binary-search-tree/?envType=problem-list-v2&envId=tree
98. Validate Binary Search Tree
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([(root, -float('inf'), float('inf'))])

        while q:
            node, low, high = q.popleft()

            # 현재 노드의 값이 정해진 범위를 벗어나면 유효하지 않은 BST입니다.
            if not (low < node.val < high):
                return False

            # 왼쪽 자식: 최솟값은 유지, 최댓값은 현재 노드의 값으로 제한
            if node.left:
                q.append((node.left, low, node.val))
            
            # 오른쪽 자식: 최솟값은 현재 노드의 값으로 제한, 최댓값은 유지
            if node.right:
                q.append((node.right, node.val, high))
        
        return True