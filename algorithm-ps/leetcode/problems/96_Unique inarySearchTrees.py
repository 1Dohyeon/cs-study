""" https://leetcode.com/problems/unique-binary-search-trees/?envType=problem-list-v2&envId=tree
96. Unique Binary Search Trees
Solved
Medium
Topics
premium lock icon
Companies
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        if n == 1:
            return dp[1]

        for nodes in range(2, n + 1):
            # i번째 노드를 루트로 설정했을 때의 경우의 수 합산
            for root in range(1, nodes + 1):
                left_nodes = root - 1 # 왼쪽 서브트리의 노드 개수
                right_nodes = nodes - root # 오른쪽 서브트리의 노드 개수
                dp[nodes] += dp[left_nodes] * dp[right_nodes] # 왼쪽 서브트리와 오른쪽 서브트리의 경우의 수 곱
                # 루트가 매번 바뀌기 때문에 모든 경우의 수를 더해줌

        
        return dp[n]
        