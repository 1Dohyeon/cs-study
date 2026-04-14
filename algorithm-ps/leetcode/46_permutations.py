"""https://leetcode.com/problems/permutations/description/
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False] * n # 사용 여부를 기록할 체크 리스트

        def backtrack(path):
            # 1. 종료 조건: 숫자를 다 뽑았으면 결과에 추가
            if len(path) == n:
                res.append(list(path))
                return

            # 2. 모든 숫자를 훑으며 선택 시도
            for i in range(n):
                # 이미 사용한 숫자라면 건너뜀
                if visited[i]:
                    continue

                # 숫자 선택 및 방문 표시
                visited[i] = True
                path.append(nums[i])

                # 다음 숫자 뽑으러 가기
                backtrack(path)

                # 3. 백트래킹: 원상복구
                path.pop()
                visited[i] = False

        backtrack([])
        return res