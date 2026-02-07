"""https://leetcode.com/problems/recover-binary-search-tree/description/?envType=problem-list-v2&envId=tree
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.


Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
"""


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 탐색에 필요한 포인터들
        self.first = None   # 첫 번째로 발견된 잘못된 노드
        self.second = None  # 두 번째로 발견된 잘못된 노드
        self.prev = None    # 이전 노드를 저장하는 포인터

        def inorder(node):
            if not node:
                return

            # 1. 왼쪽 서브트리 탐색
            inorder(node.left)

            # 2. 현재 노드 처리 (범인 찾기 로직)
            # 이전 노드가 현재 노드보다 값이 크다면 '역전 현상' 발생!
            if self.prev and self.prev.val > node.val:
                # 첫 번째 범인을 아직 못 찾았다면, 앞의 노드(prev)가 범인
                if not self.first:
                    self.first = self.prev
                    
                
                # 두 번째 범인은 항상 뒤의 노드(node)로 업데이트
                # (역전이 두 번 일어나면 두 번째 node가 최종 범인이 됨)
                self.second = node

            # 다음 노드 비교를 위해 현재 노드를 prev로 설정
            self.prev = node

            # 3. 오른쪽 서브트리 탐색
            inorder(node.right)

        # 중위 순회 시작
        inorder(root)

        # 찾은 두 노드의 값만 맞바꾸기
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val