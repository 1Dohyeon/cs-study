"""https://leetcode.com/problems/kth-smallest-element-in-a-bst/description
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        q = deque([root])

        while q:
            node = q.popleft()
            vals.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        # vals 정렬(set 중복 제거는 필요없나? tree에 중복 없으므로 필요없음)
        vals = sorted(vals)
        return vals[k-1] 


# 중위순회로 풀이
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            # 1. 최대한 왼쪽 끝까지 내려감 (가장 작은 놈 찾기)
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. 하나씩 꺼내면서 숫자를 셈
            curr = stack.pop()
            k -= 1
            
            # 3. k번째라면 바로 정답 리턴
            if k == 0:
                return curr.val
            
            # 4. 왼쪽 다 봤으니 오른쪽으로 이동
            curr = curr.right