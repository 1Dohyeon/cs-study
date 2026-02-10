""" https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=problem-list-v2&envId=tree
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
Topics
premium lock icon
Companies
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder의 값들의 인덱스를 미리 저장 (검색 최적화)
        in_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(pre_start, pre_end, in_start, in_end):
            # 범위를 벗어나면 노드가 없는 것
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # 1. preorder의 첫 번째 원소가 현재 루트
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # 2. inorder에서 루트의 위치를 찾음
            root_idx = in_map[root_val]
            
            # 3. 왼쪽 서브트리의 노드 개수 계산
            left_size = root_idx - in_start
            
            # 4. 재귀적으로 왼쪽과 오른쪽 자식 구성
            # 왼쪽: preorder(루트 다음부터 왼쪽 size만큼), inorder(시작부터 루트 전까지)
            root.left = helper(pre_start + 1, pre_start + left_size, in_start, root_idx - 1)
            # 오른쪽: preorder(왼쪽 끝 다음부터 끝까지), inorder(루트 다음부터 끝까지)
            root.right = helper(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)
            
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)