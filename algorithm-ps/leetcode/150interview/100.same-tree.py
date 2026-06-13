"""https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # None 상태까지 정밀하게 비교하기 위해 초기값 그대로 큐에 삽입
        pq = deque([p])
        qq = deque([q])

        while pq and qq:
            p_node = pq.popleft()
            q_node = qq.popleft()

            # 둘 다 None이면 구조가 일치하므로 다음 노드 검사로 패스
            if not p_node and not q_node:
                continue
                
            # 한쪽만 None이거나 값이 다르면 완벽한 불일치 (False)
            if not p_node or not q_node or p_node.val != q_node.val:
                return False

            # 자식이 있든 없든(None이든 아니든) 무조건 다 큐에 넣어서 위치를 매칭함
            pq.append(p_node.left)
            pq.append(p_node.right)
            qq.append(q_node.left)
            qq.append(q_node.right)

        return True